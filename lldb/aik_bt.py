# aik_bt.py
# LLDB integration for `aik bt`
# Depends on aik_renderer.py

import lldb
from aik_renderer import draw_stack_frame


# ---------------------------------------------------------
# Helper: resolve function name from PC
# ---------------------------------------------------------

def resolve_function_name(frame, target):
    pc = frame.GetPC()
    sc = target.ResolveSymbolContextForAddress(
        lldb.SBAddress(pc, target),
        lldb.eSymbolContextEverything
    )

    if sc.GetFunction():
        return sc.GetFunction().GetName()
    if sc.GetSymbol():
        return sc.GetSymbol().GetName()
    return "<unknown>"


# ---------------------------------------------------------
# Core LLDB command
# ---------------------------------------------------------

def aik_bt(debugger, command, exe_ctx, result, internal_dict):
    """
    LLDB command:
        aik bt [count]

    Walks stack frames and renders them using aik_renderer.
    Optional argument 'count' limits the number of frames to display.
    """

    thread = exe_ctx.GetThread()
    process = exe_ctx.GetProcess()
    target = exe_ctx.GetTarget()

    if not thread or thread.GetNumFrames() == 0:
        print("No frames available")
        return

    # Parse optional frame limit argument
    frame_limit = None
    if command.strip():
        try:
            frame_limit = int(command.strip())
            if frame_limit <= 0:
                print("Error: frame count must be a positive integer")
                return
        except ValueError:
            print(f"Error: invalid frame count '{command.strip()}'")
            return

    # Start from current frame
    frame0 = thread.GetFrameAtIndex(0)
    rbp = frame0.GetFP()
    rsp = frame0.GetSP()  # Get stack pointer for frame 0

    # Use provided limit or default to all available frames
    if frame_limit is not None:
        max_frames = min(frame_limit, thread.GetNumFrames())
    else:
        max_frames = thread.GetNumFrames()
    frame_index = 0

    while rbp != 0 and frame_index < max_frames:
        err = lldb.SBError()

        # ABI-defined layout
        old_rbp = process.ReadPointerFromMemory(rbp, err)
        if not err.Success():
            break

        ret_addr = process.ReadPointerFromMemory(rbp + 8, err)
        if not err.Success():
            break

        lldb_frame = thread.GetFrameAtIndex(frame_index)

        # Resolve function name
        fn_name = resolve_function_name(lldb_frame, target)

        # -------------------------------------------------
        # Build FRAME DATA (pure data, renderer-friendly)
        # -------------------------------------------------

        frame_data = {
            "index": frame_index,
            "name": fn_name,
            "rbp": f"0x{rbp:016x}",
            "entries": []
        }

        # Collect locals + arguments
        variables = lldb_frame.GetVariables(
            True,   # arguments
            True,   # locals
            False,  # statics
            True    # in-scope only
        )

        for v in variables:
            addr = v.GetLoadAddress()
            if addr == lldb.LLDB_INVALID_ADDRESS:
                continue

            # Get variable size based on its type
            var_size = v.GetType().GetByteSize()

            offset = addr - rbp
            frame_data["entries"].append({
                "address": f"0x{addr:016x}",
                "offset": f"<{offset:+}>",
                "value": v.GetValue() or "<optimized out>",
                "name": v.GetName(),
                "kind": "normal",
                "size": var_size
            })

        # Saved RBP (linkage)
        frame_data["entries"].append({
            "address": f"0x{rbp:016x}",
            "offset": "<+0>",
            "value": f"0x{old_rbp:016x}",
            "name": "prev_rbp",
            "kind": "rbp",
            "size": 8  # Address is 8 bytes
        })

        # Return address
        frame_data["entries"].append({
            "address": f"0x{rbp + 8:016x}",
            "offset": "<+8>",
            "value": f"0x{ret_addr:016x}",
            "name": "ret_addr",
            "kind": "normal",
            "size": 8  # Address is 8 bytes
        })

        # Sort by address first (low → high)
        frame_data["entries"].sort(
            key=lambda e: int(e["address"], 16)
        )

        # Fill gaps between entries with padding (4-byte cells)
        entries_with_padding = []
        for i, entry in enumerate(frame_data["entries"]):
            if i > 0:
                # Check for gap between previous entry and current entry
                prev_entry = frame_data["entries"][i-1]
                prev_addr = int(prev_entry["address"], 16)
                prev_size = prev_entry.get("size", 4)  # Default to 4 if not specified
                curr_addr = int(entry["address"], 16)

                # Calculate expected next address after previous entry
                expected_addr = prev_addr + prev_size
                gap = curr_addr - expected_addr

                # Add padding cells (4 bytes each) for the gap
                if gap > 0:
                    num_padding_cells = gap // 4
                    for j in range(num_padding_cells):
                        padding_addr = expected_addr + (j * 4)
                        entries_with_padding.append({
                            "address": f"0x{padding_addr:016x}",
                            "offset": f"<{padding_addr - rbp:+}>",
                            "value": "",
                            "name": "padding",
                            "kind": "padding",
                            "size": 4
                        })

            entries_with_padding.append(entry)

        frame_data["entries"] = entries_with_padding

        # Add RSP entries for frame 0
        if frame_index == 0:
            # Check if RSP matches any existing entry
            rsp_matches_existing = any(
                int(e["address"], 16) == rsp for e in frame_data["entries"]
            )

            if not rsp_matches_existing:
                # Find the first entry address (lowest)
                first_entry_addr = int(frame_data["entries"][0]["address"], 16)

                # Calculate number of 4-byte cells between RSP and first entry
                gap = first_entry_addr - rsp
                num_cells = gap // 4

                # Add padding entries for each 4-byte cell
                padding_entries = []
                for i in range(num_cells):
                    cell_addr = rsp + (i * 4)
                    padding_entries.append({
                        "address": f"0x{cell_addr:016x}",
                        "offset": f"<{cell_addr - rbp:+}>",
                        "value": "",
                        "name": "rsp" if i == 0 else "padding",
                        "kind": "rsp" if i == 0 else "padding",
                        "size": 4
                    })

                # Insert padding entries at the beginning
                frame_data["entries"] = padding_entries + frame_data["entries"]
            else:
                # Mark the matching entry as RSP
                for e in frame_data["entries"]:
                    if int(e["address"], 16) == rsp:
                        e["kind"] = "rsp"
                        e["name"] = e["name"]  # Keep original name
                        break

        # -------------------------------------------------
        # Render
        # -------------------------------------------------

        draw_stack_frame(frame_data)
        print()  # space between frames

        # Move to caller frame
        rbp = old_rbp
        frame_index += 1


# ---------------------------------------------------------
# LLDB registration
# ---------------------------------------------------------

def __lldb_init_module(debugger, internal_dict):
    # Create command container if not already present
    debugger.HandleCommand("command container add aik")

    # Register subcommand
    debugger.HandleCommand(
        "command script add -f aik_bt.aik_bt aik bt"
    )

    print("Loaded: aik bt")

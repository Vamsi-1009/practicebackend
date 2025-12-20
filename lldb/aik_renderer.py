# aik_renderer.py
# ASCII stack-frame renderer (header / body / footer separated)

ADDR_COL = 26
STACK_WIDTH = 24


# ---------------------------------------------------------
# Column helpers
# ---------------------------------------------------------

def left(text=""):
    """Left column: address / labels"""
    return f"{text:<{ADDR_COL}}"


def stack(text):
    """Stack drawing column"""
    return f"{text:<{STACK_WIDTH}}"


# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------

def draw_frame_header(frame):
    print(
        f"Frame#{frame['index']}: {frame['name']:<16} "
        + "┌                    ┐"
    )
    print(left("    ┌──────────────────┐") + "|                    |")
    print(left(f"rbp:│{frame['rbp']}│") + "|                    |")
    print(left("    └──────────────────┘") + "|                    |")
    print(left() + "|                    |")
    print(left() + "|                    |")


# ---------------------------------------------------------
# BODY
# ---------------------------------------------------------

def draw_frame_body(frame):
    entries = frame["entries"]
    num_entries = len(entries)

    for idx, e in enumerate(entries):
        # Determine separator type and RSP annotation
        rsp_annotation = ""
        if idx == 0:
            separator = "╞════════════════════╡"
        elif e["kind"] == "rbp":
            separator = "├┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┤"
        else:
            separator = "├────────────────────┤"

        if e["kind"] == "rsp":
            rsp_annotation = " ← Stack Pointer"

        # Address + offset + separator on same line
        print(left(f" {e['address']} {e['offset']}") + separator + rsp_annotation)

        # Value line - show padding for RSP/padding entries, or actual value for variables
        if e["kind"] == "rsp" and e["value"] == "":
            # RSP entry with no value (padding)
            print(left() + f"| {'padding...':<18} |")
        elif e["kind"] == "padding":
            # Additional padding cells
            print(left() + f"| {'padding...':<18} |")
        elif e["kind"] == "rsp" and e["value"] != "":
            # RSP matches an existing variable - show value and name
            print(left() + f"| {e['value']:<18} | {e['name']}")
        else:
            # Normal entries
            print(left() + f"| {e['value']:<18} | {e['name']}")

        # For 8-byte entries (addresses), add an extra empty line to span two cells
        entry_size = e.get("size", 4)
        if entry_size == 8:
            print(left() + "|                    |")

        # Bottom boundary address only for the very last entry
        if idx == num_entries - 1:
            addr = int(e["address"], 16)
            entry_size = e.get("size", 8)  # Default to 8 if not specified
            bottom_addr = addr + entry_size
            # Calculate offset from rbp (extract rbp from frame data)
            rbp = int(frame["rbp"], 16)
            bottom_offset = bottom_addr - rbp
            print(left(f" 0x{bottom_addr:016x} <{bottom_offset:+}>") + "╞════════════════════╡")


# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------

def draw_frame_footer():
    print(left() + "|                    |")
    print(left() + "|                    |")
    print(left() + "└                    ┘")


# ---------------------------------------------------------
# PUBLIC API
# ---------------------------------------------------------

def draw_stack_frame(frame):
    draw_frame_header(frame)
    draw_frame_body(frame)
    draw_frame_footer()

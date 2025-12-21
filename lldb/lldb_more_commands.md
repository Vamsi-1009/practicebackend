# LLDB More Commands

A quick reference for commonly used LLDB commands.

## Memory Read

```bash
# Basic read (default: hex, 16 bytes)
(lldb) memory read $rsp

# Read N bytes
(lldb) memory read -c 32 $rsp

# Read with size: 1, 2, 4, or 8 bytes per unit
(lldb) memory read -s 4 -c 8 $rsp    # 8 units of 4 bytes each

# Format options
(lldb) memory read -f x $rsp         # hex (default)
(lldb) memory read -f d $rsp         # decimal
(lldb) memory read -f c $rsp         # character
(lldb) memory read -f s $rsp         # string
(lldb) memory read -f i $rsp         # instruction
(lldb) memory read -f b $rsp         # binary
(lldb) memory read -f p $rsp         # pointer

# Address range
(lldb) memory read 0x7fff0000 0x7fff0020

# Read from variable address
(lldb) memory read &myvar

# Shorthand
(lldb) x -c 16 $rsp
(lldb) x/16x $rsp                    # GDB-style: 16 hex values
```

## Memory Write

```bash
# Write bytes to address
(lldb) memory write $rsp 0x41 0x42 0x43

# Write specific size values
(lldb) memory write -s 4 $rsp 0x12345678    # Write 4-byte value

# Write string (including null terminator)
(lldb) memory write $rsp "hello"

# Write to specific address
(lldb) memory write 0x7fff0010 0xff 0xee 0xdd
```

## Format Specifiers

| Flag | Format |
|------|--------|
| `-f x` | Hexadecimal |
| `-f d` | Signed decimal |
| `-f u` | Unsigned decimal |
| `-f c` | Character |
| `-f s` | C string |
| `-f i` | Disassembly |
| `-f b` | Binary |
| `-f f` | Float |
| `-f p` | Pointer |

## Memory Read Examples

```bash
# View stack as 4-byte integers
(lldb) memory read -s 4 -f d -c 8 $rsp

# View as characters (find strings)
(lldb) memory read -f c -c 64 0x555555556000

# View as pointers
(lldb) memory read -f p -c 4 $rbp
```

## Disassemble

```bash
# Disassemble a function by name
(lldb) disassemble -n main

# Disassemble from specific address
(lldb) disassemble -s 0x555555555140

# Disassemble N instructions from address
(lldb) disassemble -s 0x555555555140 -c 10

# Disassemble address range
(lldb) disassemble -s 0x555555555140 -e 0x555555555180

# Disassemble at current program counter
(lldb) disassemble -p

# Shorthand
(lldb) di -s 0x555555555140 -c 5
```

## Registers

```bash
# Read all registers
(lldb) register read

# Read specific register
(lldb) register read rsp rbp rip

# Read in different format
(lldb) register read -f d rax        # decimal
(lldb) register read -f b rax        # binary

# Write to register
(lldb) register write rax 0x1234
```

## Breakpoints

```bash
# Set breakpoint at function
(lldb) breakpoint set -n main
(lldb) b main                        # shorthand

# Set breakpoint at address
(lldb) breakpoint set -a 0x555555555140

# Set breakpoint at line
(lldb) breakpoint set -f main.c -l 10

# List breakpoints
(lldb) breakpoint list

# Delete breakpoint
(lldb) breakpoint delete 1

# Disable/enable breakpoint
(lldb) breakpoint disable 1
(lldb) breakpoint enable 1
```

## Stepping

```bash
# Step into (enter functions)
(lldb) step
(lldb) s

# Step over (skip function calls)
(lldb) next
(lldb) n

# Step out (finish current function)
(lldb) finish

# Step by instruction (not source line)
(lldb) si                            # step instruction
(lldb) ni                            # next instruction

# Continue execution
(lldb) continue
(lldb) c
```

## Variables and Expressions

```bash
# Show local variables
(lldb) frame variable
(lldb) fr v

# Show with addresses
(lldb) frame variable -L

# Show specific variable
(lldb) frame variable myvar

# Print expression
(lldb) print myvar
(lldb) p myvar

# Print in different format
(lldb) p/x myvar                     # hex
(lldb) p/d myvar                     # decimal
(lldb) p/t myvar                     # binary

# Evaluate expression
(lldb) expression myvar + 10
(lldb) expr myvar = 42               # modify variable
```

## Stack

```bash
# Show backtrace
(lldb) bt

# Show specific frames
(lldb) bt 5                          # top 5 frames

# Select frame
(lldb) frame select 2
(lldb) f 2

# Show frame info
(lldb) frame info
```

## Process and Image

```bash
# Show process info
(lldb) process status

# Show loaded libraries
(lldb) image list

# Show sections
(lldb) image dump sections

# Lookup symbol
(lldb) image lookup -n printf
(lldb) image lookup -a 0x555555555140
```

## Memory Mappings

```bash
# View process memory map (Linux)
(lldb) platform shell cat /proc/<pid>/maps
```

## Watchpoints

```bash
# Watch variable for changes
(lldb) watchpoint set variable myvar

# Watch memory address
(lldb) watchpoint set expression -- &myvar

# List watchpoints
(lldb) watchpoint list

# Delete watchpoint
(lldb) watchpoint delete 1
```

## Register Names (32-bit vs 64-bit)

| 64-bit | 32-bit | Purpose |
|--------|--------|---------|
| `$rsp` | `$esp` | Stack pointer |
| `$rbp` | `$ebp` | Base pointer |
| `$rip` | `$eip` | Instruction pointer |
| `$rax` | `$eax` | Return value |
| `$rdi` | `$edi` | 1st argument |
| `$rsi` | `$esi` | 2nd argument |
| `$rdx` | `$edx` | 3rd argument |
| `$rcx` | `$ecx` | 4th argument |

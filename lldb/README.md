# Configuration Guide

This guide explains how to set up the `aik bt` command in LLDB.

## Prerequisites

- LLDB debugger installed
- Python support enabled in LLDB

## Installation Steps

### 1. Copy the required files

Copy the following files to `~/.lldb/`:
- `aik_bt.py`
- `aik_renderer.py`

```bash
curl https://raw.githubusercontent.com/aikaryashala/practice/refs/heads/main/lldb/aik_bt.py -o ~/.lldb/aik_bt.py
curl https://raw.githubusercontent.com/aikaryashala/practice/refs/heads/main/lldb/aik_renderer.py -o ~/.lldb/aik_renderer.py
```

### 3. Configure LLDB initialization

Add the following line to your `~/.lldbinit` file:

```
command script import ~/.lldb/aik_bt.py
```

### 4. Verify the installation

Start LLDB and check if the command is loaded:

```bash
lldb
```

You should see the message:
```
Loaded: aik bt
```

## Usage

Once configured, you can use the `aik bt` command in any LLDB session:

```
(lldb) aik bt           # Show all stack frames
(lldb) aik bt 5         # Show only the first 5 frames
(lldb) aik bt 10        # Show only the first 10 frames
```

## Troubleshooting

If the command doesn't load:

1. Check that the files exist in `~/.lldb/`:
   ```bash
   ls -la ~/.lldb/
   ```

2. Verify the import line in `~/.lldbinit`:
   ```bash
   cat ~/.lldbinit
   ```

3. Check for Python errors in LLDB:
   ```
   (lldb) script print("Python is working")
   ```



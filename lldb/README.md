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
```
```bash
curl https://raw.githubusercontent.com/aikaryashala/practice/refs/heads/main/lldb/aik_renderer.py -o ~/.lldb/aik_renderer.py
```

Check that the files exist in `~/.lldb/`:
   ```bash
   ls -la ~/.lldb/
   ```

### 3. Configure LLDB initialization

3.1 If `~/.lldbinit` doesn't exist, create it:

```bash
echo "command script import ~/.lldb/aik_bt.py" >> ~/.lldbinit
```

3.2 Verify the import line in `~/.lldbinit`:
   ```bash
   cat ~/.lldbinit
   ```


## 4. To install `lldb-15` and `python3-lldb-15` on Ubuntu, run:

```bash
sudo apt update
sudo apt install lldb-15 python3-lldb-15
```

To make `lldb-15` the default `lldb`, you can use update-alternatives:

```bash
sudo update-alternatives --install /usr/bin/lldb lldb /usr/bin/lldb-15 100
```

```bash
echo "export PYTHONPATH=/usr/lib/llvm-15/lib/python3.10/dist-packages:$PYTHONPATH" >> ~/.bashrc
```

### 5. Verify the installation

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

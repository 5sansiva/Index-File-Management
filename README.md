## Index-File-Management

## Overview

This project implements a persistent, disk-based B-Tree indexing system designed to simulate how databases and operating systems manage large datasets under constrained memory environments. Each B-Tree node is stored as a fixed-size 512-byte block on disk, and at most **three nodes can be in memory at a time**, enforcing a memory constraint akin to real-world systems.

The program allows users to interact with the index through a command-line interface that supports creating index files, inserting and searching key/value pairs, loading bulk data from CSV files, printing the tree contents, and exporting entries back to CSV.

---

## File Structure

| File             | Description                                                                  |
| ---------------- | ---------------------------------------------------------------------------- |
| `main.py`        | Entry point with a command-line interface for user operations                |
| `btreeStruct.py` | Contains the `BTree` and `BTreeNode` classes for managing disk-based storage |

---

## How to Run

### Requirements

- Python 3.x
- A Unix-like environment (Linux, macOS, or WSL is recommended)
- The `main.py` file and `btreeStruct.py` should be in the same directory

### Running the Program

- Python 3.x
- Linux/macOS/WSL (recommended for consistent behavior)

### To run:

-Make sure to use the python3 command when running on the cs1.utdallas.edu server

```bash
python3 main.py
```

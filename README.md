# 📁 CS 4348 Project 3 – Disk-Based B-Tree Indexing

## 📝 Overview

This project implements a disk-based B-Tree indexing system that simulates how databases manage large indexes with limited memory. All nodes are stored as fixed-size 512-byte disk blocks, and only **three nodes can be held in memory at once**.

The system supports operations like creating index files, inserting key/value pairs, searching, loading from CSV, printing the tree, and exporting to a CSV.

---

## 🗃️ File Structure

| File             | Description                                                               |
| ---------------- | ------------------------------------------------------------------------- |
| `main.py`        | CLI to interact with the B-Tree system                                    |
| `btreeStruct.py` | Contains `BTree` and `BTreeNode` classes, handles tree logic and disk I/O |
| `input.csv`      | Optional CSV file for batch loading                                       |
| `output.csv`     | Exported key/value pairs from the index                                   |
| `*.idx`          | Index files created and managed by the system                             |

---

## ⚙️ How to Run

### Requirements

- Python 3.x
- Linux/macOS/WSL (recommended for consistent behavior)

### To run:

```bash
python3 main.py
```

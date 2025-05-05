#!/usr/bin/env python3
import os
import sys
from btree import BTree

MAGIC = b'4348PRJ3'
HEADER_SIZE = 512

class FileManager:
    def create_index_file(self, filename):
        if not filename:
            print("Error: No filename provided.")
            return

        if not filename.endswith(".idx"):
            filename += ".idx"

        if os.path.exists(filename):
            print(f"Error: File '{filename}' already exists. Operation aborted.")
            return

        header = bytearray(HEADER_SIZE)
        header[0:8] = MAGIC
        header[8:16] = (0).to_bytes(8, 'big')  # Root block ID
        header[16:24] = (1).to_bytes(8, 'big')  # Next block ID

        with open(filename, 'wb') as f:
            f.write(header)

        print(f"Index file '{filename}' created successfully.")

    def insert_into_index_file(self, filename, key, value):
        if not os.path.exists(filename):
            print(f"Error: Index file '{filename}' does not exist.")
            return

        btree = BTree(filename)
        btree.insert(key, value)
        print(f"Inserted key={key}, value={value} into '{filename}'.")

    def search_in_index_file(self, filename, key):
        if not os.path.exists(filename):
            print(f"Error: Index file '{filename}' does not exist.")
            return

        btree = BTree(filename)
        value = btree.search(key)
        if value is not None:
            print(f"Found: Key = {key}, Value = {value}")
        else:
            print(f"Key '{key}' not found in '{filename}'.")

    def load_file(self, filename, csv_file):
        if not os.path.exists(filename):
            print(f"Error: Index file '{filename}' does not exist.")
            return
        if not os.path.exists(csv_file):
            print(f"Error: CSV file '{csv_file}' does not exist.")
            return

        btree = BTree(filename)
        with open(csv_file, 'r') as f:
            for line in f:
                parts = line.strip().split(',')
                if len(parts) == 2:
                    key = int(parts[0])
                    value = int(parts[1])
                    btree.insert(key, value)
        print(f"Loaded all entries from '{csv_file}' into '{filename}'.")

    def print_index_file(self, filename):
        if not os.path.exists(filename):
            print(f"Error: Index file '{filename}' does not exist.")
            return

        btree = BTree(filename)
        for key, value in btree.traverse():
            print(f"{key} -> {value}")

    def extract_file(self, filename, output_csv):
        if not os.path.exists(filename):
            print(f"Error: Index file '{filename}' does not exist.")
            return
        if os.path.exists(output_csv):
            print(f"Error: Output file '{output_csv}' already exists.")
            return

        btree = BTree(filename)
        entries = btree.traverse()
        with open(output_csv, 'w') as f:
            for key, value in entries:
                f.write(f"{key},{value}\n")
        print(f"Extracted all entries to '{output_csv}'.")


def main():
    fm = FileManager()
    args = sys.argv[1:]

    if len(args) == 0:
        print("Usage: python project3.py <command> [arguments]")
        return

    command = args[0]

    if command == "create" and len(args) == 2:
        fm.create_index_file(args[1])

    elif command == "insert" and len(args) == 4:
        filename = args[1]
        key = int(args[2])
        value = int(args[3])
        fm.insert_into_index_file(filename, key, value)

    elif command == "search" and len(args) == 3:
        filename = args[1]
        key = int(args[2])
        fm.search_in_index_file(filename, key)

    elif command == "load" and len(args) == 3:
        fm.load_file(args[1], args[2])

    elif command == "print" and len(args) == 2:
        fm.print_index_file(args[1])

    elif command == "extract" and len(args) == 3:
        fm.extract_file(args[1], args[2])

    else:
        print("Invalid command or incorrect number of arguments.")

if __name__ == "__main__":
    main()



    
#!/usr/bin/env python3
import os
import sys
from btreeStruct import BTree

MAGIC = b'4348PRJ3'
HEADER_SIZE = 512

class FileManager:
    #Used to create a new index file
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

    #Used to insert a new key/value pair into the index file
    def insert_into_index_file(self, filename, key, value):
        if not os.path.exists(filename):
            print(f"Error: Index file '{filename}' does not exist.")
            return

        btree = BTree(filename)
        btree.insert(key=key, value=value)
        btree.close()
        print(f"Inserted key={key}, value={value} into '{filename}'.")

    #Used to search for a key in the index file
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
    
    #Used to load key/value pairs from a CSV file into the index file
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

    #Used to print all key/value pairs in the index file
    def print_index_file(self, filename):
        if not os.path.exists(filename):
            print(f"Error: Index file '{filename}' does not exist.")
            return

        btree = BTree(filename)
        for key, value in btree.traverse():
            print(f"{key} -> {value}")

    #Used to extract all key/value pairs from the index file to a CSV file
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
    while True:
        print("Welcome to the File Manager!\n")
        print("Please choose an option (enter the choice in lowercase):\n")
        print("1. create INDEX_FILE\t\t Create new index\n")
        print("2. insert INDEX_FILE KEY VALUE\t Insert a new key/value pair into current index\n")
        print("3. search INDEX_FILE KEY\t Search for a key in an index file\n")
        print("4. load INDEX_FILE CSV_FILE\t insert key/value pairs in current index in key order\n")
        print("5. print INDEX_FILE\t\t Print all the key value pairs in teh current index in key order\n")
        print("6. extract INDEX_FILE CSV_FILE\t Extract all the key/value pairs in the current index to a CSV file\n")
        print("7. exit\t\t\t\t Exit the program\n")
            
        user_input = input("Please enter your choice (or 'exit' to quit):").strip()
        args = user_input.split()

        if len(args) == 0:
            print("No command provided.")
            return

        command = args[0].lower()
        fm = FileManager()

        try:
            if command == "create" and len(args) == 2:
                fm.create_index_file(args[1])

            elif command == "insert" and len(args) == 4:
                #print(f"Using BTree class from: {BTree.__module__}.{BTree.__name__}")
                
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
            elif command == "exit":
                print("Exiting the program.")
                break   
            else:
                print("Invalid command or incorrect number of arguments.")

        except ValueError:
            print("Error: Key and value must be integers.")
        except IndexError:
            print("Error: Missing arguments for the command.")
        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()



    
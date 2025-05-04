#!/usr/bin/env python3
import os
import sys

class FileManager:
    def __init__(self):
        self.index_file = "index.txt"

    def create_index_file(self):
        with open(self.index_file, 'w') as f:
            f.write("File Name\tFile Size\tFile Path\n")
        print(f"Index file '{self.index_file}' created successfully.")

    def insert_into_index_file(self):
        file_name = input("Enter the file name: ")
        file_size = os.path.getsize(file_name)
        file_path = os.path.abspath(file_name)
        with open(self.index_file, 'a') as f:
            f.write(f"{file_name}\t{file_size}\t{file_path}\n")
        print(f"File '{file_name}' inserted into index file.")

    def search_in_index_file(self):
        search_term = input("Enter the file name to search: ")
        with open(self.index_file, 'r') as f:
            lines = f.readlines()
            for line in lines[1:]:
                if search_term in line:
                    print(line.strip())
                    return
        print(f"File '{search_term}' not found in index file.")

    def load_file(self):
        file_name = input("Enter the file name to load: ")
        if os.path.exists(file_name):
            os.startfile(file_name)
            print(f"Loading file '{file_name}'...")
        else:
            print(f"File '{file_name}' does not exist.")

    def print_index_file(self):
        with open(self.index_file, 'r') as f:
            contents = f.read()
            print(contents)

    def extract_file(self):
        file_name = input("Enter the file name to extract: ")
        with open(self.index_file, 'r') as f:
            lines = f.readlines()
            for line in lines[1:]:
                if file_name in line:
                    parts = line.strip().split('\t')
                    extracted_file_path = parts[2]
                    print(f"Extracted File Path: {extracted_file_path}")
                    return
        print(f"File '{file_name}' not found in index file.")


if __name__ == "__main__":
    print("Welcome to the File Manager!\n")
    print("Please choose an option(enter the choice in lowercase):\n")
    print("1. Create a new index file(create)\n")
    print("2. Insert into an existing index file(insert)\n")
    print("3. Search for a file(search)\n")
    print("4. Load a file(load)\n")
    print("5. Print all the contents of the index file(print)\n")
    print("6. Extract a file(extract)\n")
    user_choice = input("Enter your choice: ").strip().lower()

    FileManager f1 = FileManager()
    if user_choice == "create":
        f1.create_index_file()
    elif user_choice == "insert":
        f1.insert_into_index_file()
    elif user_choice == "search":
        f1.search_in_index_file()
    elif user_choice == "load":
        f1.load_file()
    elif user_choice == "print":
        f1.print_index_file()
    elif user_choice == "extract":
        f1.extract_file()
    else:
        print("Invalid choice! Please try again.")



    
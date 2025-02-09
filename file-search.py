import os
import re

def search_in_file(file_name, keyword):
    current_dir = os.getcwd()
    file_path = os.path.join(current_dir, file_name)
    
    if not os.path.exists(file_path):
        print("File not found in the current directory.")
        return
    
    with open(file_path, "r", errors="ignore") as f:
        found = False
        match_count = 0
        for num, line in enumerate(f, 1):
            if keyword.lower() in line.lower():
                highlighted_line = re.sub(f"(?i){keyword}", f"\033[1;31m{keyword}\033[0m", line.strip())  
                print(f"Found in line {num}: {highlighted_line}")
                found = True
                match_count += 1
        
        if not found:
            print("Keyword not found in the file.")
        else:
            print(f"\nTotal matches found: {match_count}")

file_name = input("Enter the file name (with extension): ")

while True:
    keyword = input("\nEnter keyword to search: ")
    
    search_in_file(file_name, keyword)
    
    choice = input("\nDo you want to search again? (y/n): ").strip().lower()
    if choice == "n":
        print("Exiting the program. Goodbye!")
        break

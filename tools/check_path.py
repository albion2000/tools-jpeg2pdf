import os
import re

# identify too long path and display 50 longest.

nb_long_path = 50
long_path = []

def insert_long_path(new_path):
    if (len(long_path)<nb_long_path):
        long_path.append(new_path)
        return
    else:
        for i in range(0,nb_long_path):
            if (len(new_path)>len(long_path[i])):
                long_path[i] = new_path
                return
            
def display_too_long_path(logpath_file):
    title = f"\n\n{nb_long_path} Longest path found"
    print(title)
    logpath_file.write(title+"\n")
    for i in range(0,nb_long_path):
        print(long_path[i])
        logpath_file.write(long_path[i]+"\n")

def log_long_paths(directory, max_length=255, max_file=128):
    with open("log_check_path.txt", "w", encoding="utf-8") as logpath_file: #, open("logCharset.txt", "w", encoding="utf-8") as logcharset_file:
        for root, dirs, files in os.walk(directory):
            for file in files:
                full_path = os.path.abspath(os.path.join(root, file))
                
                # Log paths with length >= 250 characters
                if len(full_path) >= max_length:
                    print(f"Long path (>= {max_length} chars): {full_path}")
                    logpath_file.write(f"PATH{len(full_path)}--"+full_path + "\n")
                    insert_long_path(full_path)

                if len(file) > max_file:
                    print(f"Long file (> {max_file} chars): {file}")
                    logpath_file.write(f"FILE{len(file)}--"+full_path + "\n")
                    insert_long_path(full_path)
                
                # Check for problematic characters for file transfers (spaces, special characters, etc.)
                # skipping 'C:'
#                if re.search(r'[^a-zA-Z0-9_\-\.\\/]', full_path[2:]):  
#                    print(f"Potentially problematic path: {full_path}")
#                    logcharset_file.write(full_path + "\n")
        display_too_long_path(logpath_file)


    
if __name__ == "__main__":
    directory_to_scan = input("Enter the path to the directory to scan : ")
    log_long_paths(directory_to_scan,250)
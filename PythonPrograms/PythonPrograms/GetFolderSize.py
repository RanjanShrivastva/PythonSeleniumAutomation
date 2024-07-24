import os

def get_folder_size(folder_path):
    total_size = 0
    for path, dirs, files in os.walk(folder_path):
        for f in files:
            file_path = os.path.join(path, f)
            total_size += os.path.getsize(file_path)
    return total_size//1024

def list_subfolder_sizes(drive_path):
    for root, dirs, files in os.walk(drive_path):
        for directory in dirs:
            folder_path = os.path.join(root, directory)
            size = get_folder_size(folder_path)
            print(f"Folder: {folder_path}")
            print(f"Size: {size} bytes\n")

# Specify the drive path you want to analyze
drive_path = "C:/"

list_subfolder_sizes(drive_path)

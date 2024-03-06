import os

path = r"C:\Users\ASUS\OneDrive\Рабочий стол\pp2\pp2\lab6\for_dirs"

# List only directories
print("Directories:")
for entry in os.scandir(path):
    if entry.is_dir():
        print(entry.name)

# List only files
print("\nFiles:")
for entry in os.scandir(path):
    if entry.is_file():
        print(entry.name)

# List all directories and files
print("\nAll Directories and Files:")
for entry in os.scandir(path):
    print(entry.name)

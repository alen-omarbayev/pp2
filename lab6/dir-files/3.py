import os

path = r"C:\Users\ASUS\OneDrive\Рабочий стол\pp2\pp2\lab6\for_dirs"
if os.path.exists(path):
    print("Directories:")
    for entry in os.scandir(path):
        if entry.is_dir():
            print(entry.name)

    print("\nFiles:")
    for entry in os.scandir(path):
        if entry.is_file():
            print(entry.name)
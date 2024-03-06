import os

path = r"C:\Users\ASUS\OneDrive\Рабочий стол\pp2\pp2\lab6\for_dirs"

print("Directories:")
for entry in os.scandir(path):
    if entry.is_dir():
        print(entry.name)

print("\nFiles:")
for entry in os.scandir(path):
    if entry.is_file():
        print(entry.name)

print("\nAll Directories and Files:")
for entry in os.scandir(path):
    print(entry.name)

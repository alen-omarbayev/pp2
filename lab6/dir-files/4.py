import os

path = r"C:\\Users\\ASUS\\OneDrive\\Рабочий стол\\pp2\\pp2\\lab6\\for_dirs\dwada.txt"
with open(path, 'r') as file:
    line_count = sum(1 for line in file)

print(f'number of lines in a file: {line_count}') 
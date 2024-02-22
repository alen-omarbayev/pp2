import re

file_path = r"C:\Users\ASUS\OneDrive\Рабочий стол\pp2\pp2\lab4\regex\row.txt"

with open(file_path, 'r', encoding='utf-8') as file:
    rows = file.readlines()

for row in rows:
    if re.findall("[a-z]+_+[a-z]|_+[a-z]+_+[a-z]|[a-z]+_+[a-z]+_|_+[a-z]+_+[a-z]+_|_+[a-z]|[a-z]+_|_+[a-z]+_|", row):
        print(row.strip())
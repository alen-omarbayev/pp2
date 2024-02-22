import re

file_path = r"C:\Users\ASUS\OneDrive\Рабочий стол\pp2\pp2\lab4\regex\row.txt"

with open(file_path, 'r', encoding='utf-8') as file:
    rows = file.readlines()

for row in rows:
    if re.findall("abb", row) or re.findall("abbb", row):
        print(row.strip())
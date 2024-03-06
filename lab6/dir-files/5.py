import os

mylist = ['a','b','c','d','e']

with open('C:\\Users\\ASUS\\OneDrive\\Рабочий стол\\pp2\\pp2\\lab6\\for_dirs\written_text.txt' , 'w') as file:
    for i in mylist:
        file.write(i + '\n')
file.close()
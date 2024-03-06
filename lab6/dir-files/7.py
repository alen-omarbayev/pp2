with open("C:\\Users\\ASUS\\OneDrive\\Рабочий стол\\pp2\\pp2\\lab6\\for_dirs\dwada.txt") as file1, open("C:\\Users\\ASUS\\OneDrive\\Рабочий стол\\pp2\\pp2\\lab6\\for_dirs\file2.txt") as file2:
    for line in file1:
        file2.write(line)
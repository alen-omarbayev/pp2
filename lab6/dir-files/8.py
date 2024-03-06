import os

path = 'C:\\Users\\ASUS\\OneDrive\\Рабочий стол\\pp2\\pp2\\lab6\\for_dirs\wasd.txt'
path_bool = os.access(path, os.F_OK)

if path_bool == False:
    print("NO")
    
elif path_bool == True:
    os.remove(path)
    print("YES")
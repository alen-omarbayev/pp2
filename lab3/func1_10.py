def uniqueList(list):
    unique_list=[]
    for num in list:
        if num not in unique_list:
            unique_list.append(num)
    print(*unique_list)

list = [int(el) for el in input().split()]
uniqueList(list)

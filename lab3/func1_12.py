def histogram(list):
    for i in range(len(list)):
        s=''
        n=0
        while n<list[i]:
            s+='*'
            n+=1
        print(s)
                
    
list = [int(el) for el in input().split()]
histogram(list)
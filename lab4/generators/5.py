def reversed_list(n):
    while n>=0:
        yield n
        n-=1

n=int(input())
for num in reversed_list(n):
    print(num)
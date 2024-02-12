def even_num(n):
    for i in range(n):
        if i%2==0:
            yield str(i)

n=int(input())

s=", ".join(even_num(n))
print(s)
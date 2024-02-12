def squares(N):
    for i in range(1,N):
        if(i**2<=N):
            yield i**2

N=int(input())
for val in squares(N):
    print (val)
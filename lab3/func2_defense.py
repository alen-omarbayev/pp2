from func2 import movies
a={}
count=0
for movie in movies:
    b=movie["category"]
    if movie["category"]==b:
        count+=1
    a[movie["category"]]=count
    
print(a)

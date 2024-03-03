words = "ABCDEFGfwfawfaf"
count=0
for letter in words:
    if ord(letter)>=65 and ord(letter)<=90:
        count+=1
print(count)
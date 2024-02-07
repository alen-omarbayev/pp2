def spy_game(nums):
    num1=num2=num3=None
    for num in nums:
        if num==0:
            if num1==None:
                num1=num
            elif num2==None:
                num2=num
        if num1!=None and num2!=None:
            if num==7:
                num3=num
    if num1!=None and num2!=None and num3!=None:
        return True
    else: 
        return False

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7])) 
print(spy_game([1,7,2,0,4,5,0])) 
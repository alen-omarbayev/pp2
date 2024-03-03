import time 
import math

def square_root(n):
    return math.sqrt(n)

n = int(input())
millisec = int(input())

time.sleep(millisec/1000)

print(f"Square root of {n} after {millisec} miliseconds is {square_root(n)}")
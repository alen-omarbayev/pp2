import math
def regular_polygon(sides, l):
    a=l/(2*math.tan(math.pi/sides))
    return (sides*l*a)/2
sides=int(input("Input number of sides: "))
l=int(input("Input the length of a side: "))
print(f"The area of the polygon is: {regular_polygon(sides, l)}")
class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0
    
class Rectangle(Shape):
    def __init__(self):
        self.length = float(input())
        self.width = float(input())
    def area(self):
        return self.length * self.width

a=Shape()
print(a.area())
b=Shape()
print(b.area())
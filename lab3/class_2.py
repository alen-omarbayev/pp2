class Shape():
    def __init__(self):
        self.area = 0
    def search_area(self):
        print(f"area: {self.area}")
class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
        self.search_area()
    
    def search_area(self):
        self.area = self.length ** 2
        super().search_area()

sqr=Square(6)
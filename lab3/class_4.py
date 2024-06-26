import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def show(self):
        print(f"Coordinates: ({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        print(f"Point moved to: ({self.x}, {self.y})")

    def dist(self, other_point):
        distance = math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)
        return distance


p1 = Point(2, 3)
p2 = Point(5, 7)

p1.show()
p2.show()

p2.move(3,1)
p2.show()

distance = p1.dist(p2)

print(distance)
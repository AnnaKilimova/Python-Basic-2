import math
class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.get_square() == other.get_square()

    def get_new_square(self, new_square):
        new_width = math.sqrt(new_square)
        new_height = new_square / new_width
        return new_width, new_height


    def __add__(self, other):
        if isinstance(other, Rectangle):
            new_square = self.get_square() + other.get_square()
            new_width, new_height = self.get_new_square(new_square)
            return Rectangle(new_width, new_height)

    def __mul__(self, n):
        new_square = self.get_square() * n
        new_width, new_height = self.get_new_square(new_square)
        return Rectangle(new_width, new_height)

    def __str__(self):
        return f"area: {self.get_square()}"

r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'

r3 = r1 + r2
assert r3.get_square() == 26, 'Test3'

r4 = r1 * 4
assert r4.get_square() == 32, 'Test4'

assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'

print(r1)
print(r2)
print(r3)
print(r4)
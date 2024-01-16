class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y


rec = Shape(3, 5)
print(rec.area())


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        super().__init__(self.radius, self.radius)

    def area(self):
        # return 3.14 * self.radius * self.radius
        return 3.14 * super().area()


c = Circle(5)
print(c.area())


class Square(Shape):
    def __init__(self, x):
        self.x = x
        super(Square, self).__init__(self.x, self.x)

    def area(self):
        return super(Square, self).area()


s = Square(5)
print(s.area())

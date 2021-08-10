from point import Point

class Line:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def slope(self):
        return ((self.b.y - self.a.y)/(self.b.x - self.a.x))

    def y_intercept(self):
        return (self.slope() * self.a.x * (-1)) + self.a.y

    def __repr__(self):
        return (f'Line({self.a}, {self.b})')

    def __str__(self):
        return (f'y = {self.slope()}x + {self.y_intercept()}')


if __name__ == '__main__':
    a = Point(3, 1)
    b = Point(5, 2)
    l = Line(a, b)
    print(l.slope())
    print(l.y_intercept())
    print(l)
    print(l.__repr__())
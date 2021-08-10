from typing import TypeVar

Point = TypeVar('Point')

class Point:
    def __init__(self, x: float, y: float, z: float = None):
        self.x = x
        self.y = y
        self.z = z

    def distance(self, other: Point) -> float:
        if self.z is None or other.z is None:
            distance = ((other.x - self.x)**2 + (other.y - self.y)**2)**0.5
            return distance
        else:
            distance = ((other.x - self.x)**2 + (other.y - self.y)**2  + (other.z - self.z)**2)**0.5
            return distance

    def midpoint(self, other) -> Point:
        if self.z is None:
            mp = Point(((self.x + other.x)/2), ((self.y + other.y)/2))
            return mp

    def __repr__(self):
        if self.z is None:
            return f"Point({self.x}, {self.y})"
        else:
            return f"Point({self.x}, {self.y}, {self.z})"




if __name__ == '__main__':
    x = Point(-6, -4)
    y = Point(1, 7)
    print("Distance between two points : ", x.distance(y))
    print("Distance between two points : ", Point.distance(x, y))
    print("Type of variable : ", type(x))
    print("Self description : ", x)
    print("The midpoint between two point : ", x.midpoint(y))
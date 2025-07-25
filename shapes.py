class Shape:
    def __init__(self, radius=None):
        self.radius = radius

    def area(self):
        print("The area method is not implemented")


class Circle(Shape):
    def __init__(self, radius):
        super().__init__(radius)

    def area(self):
        return 3.14 * self.radius * self.radius


class Rect(Shape):
    def __init__(self, l, b):
        super().__init__()  # radius is not needed for rectangle
        self.l = l
        self.b = b

    def area(self):
        return self.l * self.b


def main():
    radius = int(input("Enter the radius: "))
    c = Circle(radius)
    print("Area of Circle:", c.area())

    l = int(input("Enter length: "))
    b = int(input("Enter breadth: "))
    r = Rect(l, b)
    print("Area of Rectangle:", r.area())


main()

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

# Create object
circle1 = Circle(7)

print("Area of circle:", circle1.area())
print("Perimeter of circle:", circle1.perimeter())

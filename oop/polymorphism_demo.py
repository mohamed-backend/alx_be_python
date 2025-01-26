import math

# Base Class: Shape
class Shape:
    def area(self):
        # This method should be overridden in subclasses
        raise NotImplementedError("Subclasses must implement the area method")

# Derived Class: Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        # Override to calculate the area of a rectangle
        return self.length * self.width

# Derived Class: Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        # Override to calculate the area of a circle using π * radius^2
        return math.pi * (self.radius ** 2)
from polymorphism_demo import Shape, Rectangle, Circle

def main():
    shapes = [
        Rectangle(10, 5),  # Rectangle with length 10 and width 5
        Circle(7)          # Circle with radius 7
    ]

    # Polymorphism in action: Loop through shapes and calculate the area
    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

if __name__ == "__main__":
    main()

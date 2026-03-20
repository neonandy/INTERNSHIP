#one parent multiple child classes

class Person:

    def __init__(self, name):
        self.name = name


class Student(Person):

    def __init__(self, name, marks):
        super().__init__(name)   # calling parent constructor
        self.marks = marks


# Usage
s = Student("Nandan", 85)

print(s.name)
class Shape:
    def __init__(self, color):
        self.color = color

    def describe(self):
        print(f"I am a {self.color} shape")

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width  = width
        self.height = height

    def area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, color, base, height):
        super().__init__(color)
        self.base   = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

c = Circle("red", 5)
r = Rectangle("blue", 4, 6)

c.describe()    # "I am a red shape"  ← from Shape
print(c.area()) # 78.5               ← own method
print(r.area()) # 24                 ← own method
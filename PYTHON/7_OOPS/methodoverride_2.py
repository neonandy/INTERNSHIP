class Shape:
    def draw(self):
        print("Drawing shape")

class Circle(Shape):
    def draw(self):  # overriding
        print("Drawing circle")

# Usage
obj = Circle()
obj.draw()

obj = Shape()
obj.draw()

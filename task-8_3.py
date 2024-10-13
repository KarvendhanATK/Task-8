#Task-8.3
#From the given List create two class Methods Area and Perimeter
# which will be going to calculate the Area and Perimeter.

import math

class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

# Circle radius 1
NewCircle = Circle(1)

# Print area and perimeter
print(NewCircle.area())
print(NewCircle.perimeter())

#Task-8.1
#Using the Python's Object Oriented Programming Scheme (OOPS) 
#kindly complete the following tasks which is given as below :- 
#Create a Python Class called Circle with Constructor which will take a List as an argument for the task. 
# The List is [10, 501, 22, 37, 100, 999, 87, 351]
list=[10, 501, 22, 37, 100, 999, 87, 351]
class Circle:
    def __init__(self, radii):
        self.radii = radii

    def display_radii(self):
        print("Radii of circles:", self.radii)

radii_list = [10, 501, 22, 37, 100, 999, 87, 351]
circle = Circle(radii_list)
circle.display_radii()

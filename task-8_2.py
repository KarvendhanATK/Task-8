#Task-8.2
#Using the Python's Object Oriented Programming Scheme (OOPS) 
# kindly complete the following tasks which is given as below :
# Create proper member variables inside the task if required and use them when necessary. 
# For example for this task create a class private variable named pi = 3.141

class MyClass:
    # Private class 
    __pi = 3.141
   
    def __privMeth(self):
        print("I’m inside class MyClass")

    def hello(self):
        print("Private Variable value:", MyClass.__pi)

# object of MyClass
foo = MyClass()
foo.hello()
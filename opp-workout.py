

# Exercise 1

# 1.1
# Write a Rectangle class in Python language, allowing you to build
# a rectangle with length and width attributes.

class rectangle:

    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
# 1.2
# Create a Perimeter() method to calculate the perimeter of the rectangle and
# a Area() method to calculate the area of the rectangle
    def perimeter(self):
        return (2*self.length)+(2*self.breadth)
    def area(self):
        return self.length*self.breadth
# 1.3
# Create a method display() that display the length, width, perimeter and
# area of an object created using an instantiation on rectangle class.

    def display(self):
        print(f"length : {self.length} \n"
              f"breadth : {self.breadth} \n"
              f"perimeter : {self.perimeter()} \n"
              f"area : {self.area()}")
# 1.4
# Create a Parallelepipede child class inheriting from the Rectangle class
# and with a height attribute
# and another Volume() method to calculate the volume of the Parallelepiped.

class perallelepipede(rectangle):

    def __init__(self,length,breadth,height):
        rectangle.__init__(self,length,breadth)
        self.height=height
    def volume(self):
        return print(self.length*self.breadth*self.height)


per=perallelepipede(10,10,10)
per.display()
per.volume()
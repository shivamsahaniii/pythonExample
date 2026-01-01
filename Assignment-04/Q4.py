# Concept: Function Overriding
# . Create a class Shape with a method area().
# Create subclasses Circle, Rectangle, and Triangle that override the area() method.

class Shape:
    def area(self):
        return self
    
class Circle(Shape):
    def area(self, radius):
        pia = 3.14
        area = pia * radius ** 2
        print(f"The area of the Circle is {area} cm")

class Rectangle(Shape):
    def area(self, width, height):
        area = width * height
        print(f"The area of the Rectangle is {area} cm")
    
class Triangle(Shape):
    def area(self, base, height):
        area = (base * height) / 2
        print(f"The area of the Triangle is {area} cm")   

print(f"1. To calculate area of Circle \n2. To calculate area of Rectangle \n3. To calculate area of Triangle")
options = input("Choose the option: ")

match options:
    case '1':
        radius = int(input("Enter the radius (in cm): "))
        cic = Circle()
        cic.area(radius)

    case '2':
        width = int(input("Enter the base of Rectangle (in cm): "))
        height = int(input("Enter the height of the Rectangle (in cm): "))
        rec = Rectangle()
        rec.area(width, height)

    case '3':
        base = int(input("Enter the base of Triangle (in cm): "))
        height = int(input("Enter the height of the Triangle (in cm): "))
        tri = Triangle()
        tri.area(base, height)
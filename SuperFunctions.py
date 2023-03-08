"""The super() function in Python is used to refer to the parent class of a class, and allows you to call its methods."""
"""This is useful when you have a subclass that inherits from a parent class and you want to access a method that is defined in the parent class."""
#EXAMPLE 1
class Parent:
    def __init__(self):
        self.parent_var = "I am the parent"

    def parent_method(self):
        print("This is a method in the parent class")

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.child_var = "I am the child"

    def child_method(self):
        print("This is a method in the child class")

child_obj = Child()
child_obj.child_method() # This is a method in the child class
child_obj.parent_method() # This is a method in the parent class
  #EXAMPLE 2.
class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        pass

class Circle(Shape):
    def __init__(self, x, y, r):
        super().__init__(x, y)
        self.r = r

    def area(self):
        return 3.14 * self.r ** 2

class Rectangle(Shape):
    def __init__(self, x, y, w, h):
        super().__init__(x, y)
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

circle = Circle(0, 0, 5)
rectangle = Rectangle(0, 0, 10, 5)

print("Circle area:", circle.area())
print("Rectangle area:", rectangle.area())
 #ie, the above example can also mean as below.
class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        pass #pass function is used if no output, return values is needed. Th pass is added to avoid None type errors

class Circle(Shape):
    def __init__(self, x, y, r):
        super().__init__(x, y)
        self.r = r

    def area(self):
        return 3.14 * self.r ** 2

class Rectangle(Shape):
    def __init__(self, x, y, w, h):
        super().__init__(x, y)
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h
"""Objects creation , calling then printing"""
circle1 = Circle(0, 0, 5)
rectangle1 = Rectangle(0, 0, 10, 5)
circle2 = Circle(1, 2, 6)
rectangle2 = Rectangle(1, 2, 15, 5)

print("Circle areas for circle 1  :", circle1.area())
print("Rectangle areas are :", rectangle1.area() )
print("for circle 2 is " ,circle2.area())
print("for rectangle 2 is " ,rectangle2.area())
 #Example 3.
class Person:
   def __init__(self, name, age):
       self.name=name
       self.age=age
   def display(self):
       print('Name:', self.name)
       print('Age:', self.age)
class Employee(Person):
   def __init__(self, name, age, empno, address):
       super().__init__(name, age)
       self.empno=empno
       self.address =address

   def display(self):
       super().display()
       print('Emp No:', self.empno)
       print('Address:', self.address)

e1=Employee('Neethu',16,111,"Delhi")
e1.display()

#Example 4.
"""A simple program that welcomes any given student to a class of a given year"""
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2019)
x.welcome()
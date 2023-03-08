"""Static Method"""
# A static method is a method that belongs to a class rather than an instance of the class. It does not have access to the instance or class variables and does not modify the state of the class or instance.
#  To define a static method, you can use the @staticmethod decorator:
"""Class method"""
# Class Method
# A class method is a method that belongs to a class rather than an instance of the class. It has access to the class variables, but not to the instance variables.
#  To define a class method, you can use the @classmethod decorator:
"""Static method Example."""
class MyClass:
    @staticmethod
    def my_static_method(arg1, arg2):
        # do something block
     MyClass.my_static_method(arg1, arg2)
"""Class method example"""
class MyClass:
    class_variable = 0

    @classmethod
    def my_class_method(cls, arg1): #the cls is refferencing to the class variablle, just like the use of self
        cls.class_variable += arg1
         # do something block 
        MyClass.my_class_method(arg1)
"""A comprehensive example  on the above"""
class MyClass:
    class_variable = 0

    @classmethod
    def add_to_class_variable(cls, value):
        cls.class_variable += value

    @staticmethod
    def multiply_two_numbers(num1, num2):
        return num1 * num2

# Using the class method to modify the class variable
MyClass.add_to_class_variable(5)
MyClass.add_to_class_variable(10)
print(MyClass.class_variable) # Output: 15

# Using the static method to multiply two numbers
result = MyClass.multiply_two_numbers(5, 10)
print(result) # Output: 50
"""Another  compehensive example"""
class Math:
    PI = 3.14159  # Class variable

    @staticmethod
    def add_numbers(x, y):
        return x + y

    @classmethod
    def circle_area(cls, radius):
        return cls.PI * radius ** 2

# Using the static method to add two numbers
result = Math.add_numbers(5, 10)
print(result) # Output: 15

# Using the class method to calculate the area of a circle
area = Math.circle_area(2)
print(area) # Output: 12.56636

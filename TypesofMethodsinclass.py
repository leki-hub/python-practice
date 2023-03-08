#TOPIC TYPES OF METHODS IN CLASS IN PYTHON.
   # These are : Instance Methods,Class Methods,Static Methods
 # 1 INSTANCE METHODS. Example 1 below. nb Instance methods are methods which act upon the instance variables of the class.The first parameter for instance methods should be self variable which refers to instance. Along with the self variable it can contain other variables as well.
class Demo:
   def __init__(self, a):
       self.a=a
   def m(self):
       print(self.a)
d=Demo(10)
d.m()
      # Example 2 of instance methods. Setter and Getter methods in Python:- Setter methods can be used to set values to the instance variables.Their main aim is to only set values to instance variables, hence they don’t return anything.
                                                       #:-Getter methods are used to get the values of instance variables. They return the value in the instance variable.
           #Setter methods example below
class Customer:
   def set_name(self, name):
       self.name=name
   def set_id(self, id):
       self.id=id
c=Customer()
c.set_name("Balayya")
c.set_id(1)
print("Your ID is",  c.id)
print("Your Name  is" , c.name) # or alternatively you can have one print line print("Your Name  is" , c.name , " and ID " ,c.id)
           #Getter methods example below 
class Customer:
   def set_name(self, name):
       self.name=name
   def set_id(self, id):
       self.id=id

   def get_name(self):
       return self.name

   def get_id(self):
       return self.id

c=Customer()
c.set_name("Balayya")
c.set_id(1)

print("My name is: ", c.get_name())
print("My id is: ", c.get_id())
 #2 CLASS METHODS.- NB ;Class methods are methods which act upon the class variables or static variables of the class. 
         #   ...Class methods should be declared with @classmethod. Just as instance methods have ‘self’ as the default first variable, class method should have ‘cls’ as the first variable. 
          # / NB, Class methods are rarely used in python
     #Example below
class Pizza:
   radius=200
   @classmethod
   def get_radius(cls):
       return cls.radius
print(Pizza.get_radius())
  #3 STATIC VARIABLES. Inside these methods we won’t use any instance or class variables. No arguments like cls or self are required at the time of declaration.
    # /...We can declare static method explicitly by using @staticmethod decorator.
    #Example below
class Demo:
   @staticmethod
   def sum(x, y):
       print(x+y)
   @staticmethod
   def multiply(x, y):
       print(x*y)
Demo.sum(2, 3)
Demo.multiply(2,4)
#  4 NESTED CLASSES IN PYTHON. -A class inside another class are called nested classes.
  #   Example below
class A:

   def __init__(self):
       print("outer class object creation")
   class B:
       def __init__(self):
           print("inner class object creation")
       def m1(self):
           print("inner class method")
a=A()
b=a.B()
b.m1()

   #Subtopic notes on overiding-a concept in polymorphism, 
"""For every operator like+,-,+,=,!=,<,//,> ,etc ; Magic methods are available. magic methods are special methods that start and end with double 
To overload any operator, we should override that Method in our class."""
#Its in the sense of overiding since there is another different magic method.THAt is the _init_() constructor.
"""Magic methods are used to define how instances of a class behave in response to certain operations, such as arithmetic operations (+, -, *, /), comparison operations (==, !=, <, <=, >, >=), and others. """
# """Examples, on use of magic method""" 
#The execution of this snippet that has >,<,<=,>=.<=  
#... operants is not possible until we use magic methods associated., shown in example 1.1
       #Example 1.
class Student:
   def __init__(self, name, marks):
       self.name=name
       self.marks=marks


s1=Student("Samvida", 100)
s2=Student("Surya", 200)
print("s1>s2 =", s1>s2)
print("s1<s2 =", s1<s2)
print("s1<=s2 =", s1<=s2)
print("s1>=s2 =", s1>=s2)
 #Output- TypeError: ">" not supported between instances of student and student
   #Example 1.1
class Student:
   def __init__(self, name, marks):
       self.name=name
       self.marks=marks
   def __gt__(self, other):#greater than method is overiding instance variabeles initialized.
       return self.marks>other.marks
   def __lt__(self, other):# less than method is overiding instance variabeles initialized.
       return self.marks<=other.marks


s1=Student("Samvida", 100)
s2=Student("Surya", 200)
print("s1>s2 =", s1>s2)
print("s1<s2 =", s1<s2)
#Output :  s1>s2 = False 
#          s1<s2 = True
"""Nb ; magic methods has self  and other for variable constructors.The self refers to a variable already declared by the _init_ constructor """

 #EXAMPLE 2.1 
"""Another simple example below"""
#The below code will not be executed
class Book:
   def __init__(self, pages):
       self.pages=pages

b1=Book(100)
b2=Book(200)

print(b1 + b2)
  #Example 2.2 
  #This will be executed.
class Book:
   def __init__(self, pages):
       self.pages=pages
   def __add__(self, others):
       return self.pages + others.pages   
b1=Book(100)
b2=Book(200)

print(b1 + b2)
#Example
class Student:
   def __init__(self, name, rollno):
       self.name=name
       self.rollno=rollno

   def __str__(self):
       return 'This is Student object with name {} and roll no {}'.format(self.name, self.rollno)
s1=Student('Ram',10)
s2=Student('Rahim' ,12)
print(s1)
print(s2)

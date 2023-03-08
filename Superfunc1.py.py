"""Scenarios where super function can be used """
 #.- When the Parent class and Child class have same methods such that its methods might be wished to be accesed temporarily
    #Check the below 2 syntaxes
"""for calling parent method function"""
"""Scenario 1""" 
   #Example 1(i)
class A:
   def m1(self):
       print("Super class A: m1 method")
class B(A):
   def m1(self):
       print("Child class B: m1 method")
b=B()
b.m1()
    #output- Child class B: m1 method
     #Example 1 (ii)
class A:
   def m1(self):
       print("Super class A: m1 method")
class B(A):
   def m1(self):
       print("Child class B: m1 method")
       super().m1()
b=B()
b.m1()
  #Output- Child class B: m1 method /n  Super  class A: m1 method
"""Scenario 2 ."""
"""The below syntax is also okay for calling parent initialization function"""
class A:
   def __init__(self):
       print("super class A constructor")

class B(A):
   def __init__(self):
       print("Child class B constructor")
       super().__init__()
  
b=B()
"""Scenario 3"""
"""Calling super class variable from child class method using super()"""
  #Example 1.
class A:
   x=10
   def m1(self):
       print("Super class A: m1 method")
class B(A):
   x=20
   def m1(self):
       print('Child class x variable', self.x)
       print('Super class x variable', super().x)
b=B()
b.m1()
"""look at the below general example"""
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
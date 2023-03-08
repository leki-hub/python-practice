"""ABSTRACTION AND INTERFACE"""
   #ABSTRACTION, EXAMPLE 1
from abc import ABC, abstractmethod
class MyabstractClass(ABC):
   @abstractmethod
   def myabstractmethod(self):
     pass
   def concretemethod(self):
       print("This is an implementable method")
class MyConcreteClass(MyabstractClass):
    
    def myabstractmethod(self):
        print("This is the implementation of the abstract method in the concrete class.")

my_concrete_object = MyConcreteClass()
my_concrete_object.myabstractmethod()
my_concrete_object.concretemethod()

   #INTERFACE example on above .
from abc import ABC, abstractmethod
class MyabstractClass(ABC):
   def __init__(self , name , age):
     self.name= name
     self.age= age
   @abstractmethod
   def myabstractmethod():
    pass
   @abstractmethod
   def concretemethod(self):
      pass
    #    print("This is an implementable method")
class MyConcreteClass(MyabstractClass):
    
    def myabstractmethod(self):
        print("This is the implementation of the abstract method in the parent class." ,self.name, self.age )
    def concretemethod(self):
       print(" Another abstract method from the parent class" , self.age, self.name )
my_concrete_object = MyConcreteClass("Emma" , 27)
my_concrete_object.myabstractmethod()
myconcreteobj2= MyConcreteClass("Sam", 29)
myconcreteobj2.concretemethod()
 #Abstraction example, where we have multi-level inheritance
from abc import ABC, abstractmethod

#Abstract Class
class Bank(ABC):
   def bank_info(self):
       print("Welcome to bank")
   @abstractmethod
   def interest(self):
       "Abstarct Method"
       pass
#Sub class/ child class of abstract class
class SBI(Bank):

   def balance(self):
       print("Balance is 100")

class Sub1(SBI):
   def interest(self):
       print("In sbi bank interest is 5 rupees")

s= Sub1()
s.bank_info ()
s.balance()
s.interest()
 #Example 3.
from abc import ABC, abstractmethod
class One(ABC):
   @abstractmethod
   def calculate(self, a):
       pass
   def m1(self):
       print("implemented method")

class Square(One):
   def calculate(self, a):
       print("square: ", (a*a))

class Cube(One):
   def calculate(self, a):
       print("cube: ", (a*a*a))
s = Square()
c = Cube()
s.calculate(2)
c.calculate(2)
"""other INTERFACE examples"""
#Example 2
from abc import ABC, abstractmethod
class Bank(ABC):
   @abstractmethod
   def balance_check(self):
       pass
   @abstractmethod
   def interest(self):
       pass

class SBI(Bank):
   def balance_check(self):
       print("Balance is 100 rupees")
   def interest(self):
       print("SBI interest is 5 rupees")


s = SBI()
s.balance_check()
s.interest()
#Example 3
from abc import *
class DBInterface(ABC):
   @abstractmethod
   def connect(self):
       pass
   @abstractmethod
   def disconnect(self):
       pass

class Oracle(DBInterface):
   def connect(self):
       print('Connecting to Oracle Database...')
   def disconnect(self):
       print('Disconnecting to Oracle Database...')

class Sybase(DBInterface):
   def connect(self):
       print('Connecting to Sybase Database...')
   def disconnect(self):
       print('Disconnecting to Sybase Database...')   

dbname=input('Enter Database Name either Oracle or Sybase:')
classname=globals()[dbname]
x=classname()
x.connect()
x.disconnect()
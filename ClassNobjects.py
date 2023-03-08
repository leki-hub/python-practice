#TOPIC : CLASS AND OBJECTS IN PYTHON.
           #SUBTOPIC 1. Instant variables in python.
    #Example 1, that does not use methods.It is important to use a constructor def __init__(self, id): so that we can initialize variables of objects.
class Employee:
   def __init__(self, id):# self must always we used so it can be used to refer to the variables/parameters like id,
       self.id = id
       print("Employee id is: ", self.id)

Employee(1)
Employee(2)
   #Example 2. #An example where the variable is intialized to a given value.
class Employee:
   def __init__(self):
       self.id = 1 #Here, the id variable has been initialized to 1. Thus, both e1, e2, e3 will give the same output at console,
       print("Employee id is: ", self.id)

e1 = Employee()
e2 = Employee()
e3 = Employee()
  #Example 3
class Employee:
   def __init__(self, id,name):
       self.id=id
       self.name=name

   def display(self):
       print("Hello my id is :", self.id)
       print("My name is :", self.name)

e1=Employee(1, 'Nithin')#Nb, you call without assigning a variable e2
e1.display() #This line is not neccesary
e2=Employee(2, 'Arjun') #Nb, you call without assigning a variable e2.
e2.display()#This line is not neccessary.
   #Example 3-Case of instant variables #We can declare variable in a class inside constructor function as shown below.
class Employee:
   def __init__(self):
       self.eno=1
       self.ename="Nithya"
       self.esal=100
e=Employee()

print("Employee number: ",e.eno)
print("Employee name: ", e.ename)
print("Employee salary: ", e.esal)
print(e._dict_) # This line is only neccesary if want to change output into a dictioanry function.NB, Every object in Python has an attribute denoted as __dict__, which python creates internally. This displays the object information in dictionary form. It maps the attribute name to its value.
   #Ecample 3(1) Declare variable in a class inside method function ,as shown below.
class Student:
   def m1(self):
       self.a=11
       self.b=21
       self.c=34
       print(self.a)
       print(self.b)
       print(self.c)

s= Student()
s.m1()
print(s.__dict__) # Is not a must   , but only if we need the console to also give a dictionary.Every object in Python has an attribute denoted as __dict__, which python creates internally. This displays the object information in dictionary form. It maps the attribute name to its value.
# Evample 3 (ii) Declaring instance variables using object name
class Test:
   def __init__(self):
       print("This is constructor")
   def m1(self):
       print("This is instance method")

t=Test()
t.m1()
t.a=10
t.b=20
t.c=55
print(t.a)
print(t.b)
print(t.c)
print(t.__dict__)
  # SUB TOPIC 2 : STATIC VARIABLES IN PYTHON -opposite of instant variable above.
   #If the value of a variable is not changing from object to object, such types of variables are called static variables or class level variables.
     # ...We can access static variables either by class name or by object name. Accessing static variables with class names is highly recommended than object names.
#Accessing static variables outside of class-example 1 below
class Student:
   college_name='GITAM'
   def __init__(self, name, id):
       self.name=name
       self.id=id
s1=Student('Nithya', 1)
s2=Student('Anushka', 2)

print("Studen1 info:")
print("Name: ", s1.name)
print("Id : ", s1.id)
print("College name n : ", Student.college_name)

print("\n")
print("Studen2 info:")
print("Name: ",s2.name)
print("Id : ",s2.id)
print("College name : ", Student.college_name)   
#Accessing static variables with object name -Example below
class Student:
   college_name='GITAM'
   def __init__(self, name, id):
       self.name=name
       self.id=id
s1=Student('Nithya', 1)
s2=Student('Anushka', 2)

print("Studen1 info:")
print("Name: ", s1.name)
print("Id : ", s1.id)
print("College name n : ", s1.college_name)

print("\n")
print("Studen2 info:")
print("Name: ",s2.name)
print("Id : ",s2.id)
print("College name : ", s1.college_name)
      #DECLARING STATIC VARIABLES. Lets learn how to declare Static variables in class
         #/ i- Inside class and outside of the method. This is the preferred way.
         #/ ii- Inside constructor
         #/- iii- Inside instance method
         # /- iv- Inside class method
         # /-Inside static method
  # Declaring static variable inside class and outside of the method -example below. Nb,This is the preferred way.
class Demo:
   a=20
   def m(self):
       print("this is method")
print(Demo.__dict__)
   #Declaring static variable inside constructor
class Demo:
  
   def __init__(self):
       Demo.b=20
d = Demo()
print(Demo.__dict__)
    #Declaring static variable inside instance method
class Demo:
  
   def m1(self):
       Demo.b=20
obj=Demo()
obj.m1()
print(Demo.__dict__)
   #Declaring static variable inside class method- to be dicused in next chapters
     # NB, A method inside a class with @classmethod decorator is called a class method. We will discuss this in next chapters. Inside the class method we can declare and initialize static variables by using the class’s name.
  #example 1  below
class Demo:
   @classmethod
   def m2(cls):
       Demo.b=30
obj=Demo()
obj.m2()
print(Demo.__dict__)
  #Example 2 - static variable inside class method by using cls
class Demo:
   @classmethod
   def m2(cls):
       cls.b=30
obj=Demo()
obj.m2()
print(Demo.__dict__)
#Accessing a static variables Inside static method- to be dicused in next chapters
  #Example below
class Demo:
   a=10
   @staticmethod
   def m1():
       print(Demo.a)
obj=Demo()
obj.m1()
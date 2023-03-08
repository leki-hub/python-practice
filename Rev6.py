#Declaring instance variables using object name
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

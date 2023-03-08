"""Different Approaches of Calling Method of a specific Class"""
  #1  NameOfTheClass.methodname(self) – It will call super class method
  #2 super(NameOfTheClass, self).methodname – It will call the method of super class of mentioned class name.
"""Case 1 """
   #Example 
class A:
   def m1(self):
       print('m1() method from A class')
class B(A):
   def m1(self):
       print('m1() method from B class')
class C(B):
   def m1(self):
       print('m1() method from C class')
class D(C):
   def m1(self):
       print('m1() method from D class')
class E(D):
   def m1(self):
       A.m1(self)

e=E()
e.m1()
"""Case 2"""
class A:
   def m1(self):
       print('m1() method from A class')
class B(A):
   def m1(self):
       print('m1() method from B class')
class C(B):
   def m1(self):
       print('m1() method from C class')
class D(C):
   def m1(self):
       print('m1() method from D class')
class E(D):
   def m1(self):
       #A.m1(self)
       super(D, self).m1()
      
e=E()
e.m1()
"""Different Approaches for Calling same method of a specific superclass"""
# Approach 1-  ; NameOfTheClass.methodname(self)
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
    print("Yes we can")
    B.m1(self) #eg, if we want for class B. We can also use A.m1() for class A, C.m1() for class C and so on.

e=E()
e.m1()

# Aproach 2.- super(NameOfTheClass, self).methodname – It will call the method of super class of mentioned class name
#   on the above similar snippet, 
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
       super(D, self).m1() #This is if to call for class D. We can also use Super(A, self).m1() for class A, etc
      
e=E()
e.m1()
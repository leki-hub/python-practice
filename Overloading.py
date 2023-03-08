"""MAGIC METHODS contd notes"""
#We can use the same operator or methods for different purposes. There are 3 types of overloading:
"""1 Operator Overloading
   2 Method Overloading
   3 Constructor Overloading"""
#If we use the same operator for multiple purposes, then it is nothing but operator overloading.
    #Example 1.
print(10+20)
print("Python" + "Programming")
print([1,2,3]+[4,5,6])
    #Example 2
print(10*20)
print("Python"*3)
print([1,2,3]*3)
   #Example 3
class Book:
   def __init__(self, pages):
       self.pages=pages

b1=Book(100)
b2=Book(200)
print(type(b1))
print(type(b2))

print(type(b1.pages))
print(type(b2.pages))

print(b1.pages + b2.pages)# will give same result as line 28
print((b1.pages).__add__(b2.pages)) #This line is just a demo on how magic methods work
     #Example 4.1
class Book:
   def __init__(self, pages):
       self.pages=pages
   def __add__(self, others):
       return self.pages + others.pages   
b1=Book(100)
b2=Book(200)

print(b1 + b2)
""" The below Example 42. snippet will give an error but the one above ,ie 4.1 will not"""
 #Example 4.2
class Book:
   def __init__(self, pages):
       self.pages=pages

b1=Book(100)
b2=Book(200)

print(b1 + b2)

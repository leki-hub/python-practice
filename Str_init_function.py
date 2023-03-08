"""The __str__() function controls what should be returned when the class object is represented as a string. """
#Example belw.
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    """ On below function,we can  use either .__str__ or __repr__"""
    def __str__(self):#Is used if a string is to be returmed. Otherwise if only display ie print was needed, 
      return " You can " f"{self.name}({self.age})"    

p1 = Person("John", 36)
print(p1)
#Example 2
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
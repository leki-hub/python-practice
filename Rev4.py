class Employee:
   def __init__(self,name):
       self.id=1
       self.names=name
       print("Hello my id  and  name is :", self.id , "and : " , self.name)
Employee('Nithin')
Employee('Arjun')
#Example 2.
class Employee: 
   def __init__ (self , num):#This is a none parameterized constructor
      self.num = num
      
      print("constructor" , self.num)

emp1= Employee(4 )

emp1.__init__(7) #This function call line is not neccesary.we can call using the class name employee call functionas in line 14.

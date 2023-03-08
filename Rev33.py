class Employee:
    def __init__(self,name, age , salary, gender):
        self.names= name
        self.age= age
        self.salary= salary
        self.gender= gender
        self.email= self.generateEmail()
    def generateEmail(self):#lets create a function that creates emails.
        return f"{self.names}@gmail.com"
    def ShowDetails(self):
        print(self.names, self.age,self.salary, self.gender,self.email)    
    
obj= Employee("John",10, 100000, "Male")
obj.ShowDetails()
print(obj.generateEmail())
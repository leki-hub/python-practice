class Parent:
      def _init_(self):
          self.var1 = "This is a parent class initialization"
      def parentMethods(self):
           print("This is a method in the parent class")
class Child(Parent):
       def _init_ (self):
           self.var = " This is a child class initialization"
           super().__init__() #This is to call the parent class initialization for use if needed
       def Childmethods(self):
            print("This is  methods in the child class")
        
obj= Child() #Class object creation
obj.Childmethods() #Calling the method in child
obj.parentMethods() #Calling the methods in Parent
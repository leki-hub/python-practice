def calculator():
   while True:
       Operation= input("Enter the operation between: ( +, -,*, / ) ")
       if  Operation not in [" +", "-", "*" , "/"]: #this is a list of the posible  objects in the opetion variable
         print("You have entered an incorect operator , : Please enter the correct operator")
         continue
       Number1 = int(input("Enter the first number : "))
       Number2 = int(input(" Enter the second number :"))
       if Operation == "+":
         Result = Number1 +Number2
       elif Operation == "-":
         Result = Number1-Number2
       elif Operation == "*":
         Result = Number1 +Number2
       else:
        Result = Number1/Number2
        Repeatagain= input("Do you want to repeat the process again [Yes or no] :  ?")
        if Repeatagain != " Yes":
         break
calculator()
        
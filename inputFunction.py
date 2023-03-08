#There are 3 types of control statements in python. sequential, conditional and looping. The below ecample is for conditional.We have made a program that accepts data through the input function then performs conditions after the other.
print("Please enter the values from 0 to 4")
x=int(input("Enter a number: "))

if x==0:
       print("You entered:", x ,"Fail")
elif x==1:
       print("You entered:", x , "pass")
elif x==2:
      print("You entered:", x ,"Tried")
elif x==3:
       print("You entered:", x ,"good")
elif x==4:
       print("You entered:", x ,"Excellent")
else:
       print("Beyond the range than specified")
       #Example 2
user_name = 'emma'
x=input("Enter a name: ")
if x== user_name:
   print("The name is valid")
else:
   print("The name is invalid")
   # Example on how to craeat a user-defined function.
   def calculate_area(length, width):
    area = length * width
    return area

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

print("The area of the rectangle is:", calculate_area(length, width))

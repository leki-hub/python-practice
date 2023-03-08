#To find substring in a string example
 # USE OF MEMBERSHIP OPERATORS examples
x = input("Enter main string  :  ")
y= input(" Enter the other  other word : ")
if y in x:
    print( y, "Is  found in " , x )
else:
    print( y,"Is not found in " , x)
    #other simple examples, nb  in and not in are caled membership operators
print('s' in 'python')  # The output will be : 'False' , ie beacuse the substring 's' is not in the main string 'python'
print('p' in 'python')# The output will be : 'True'
 # Example. User validation.

user_name = "rahul"
name = input("Please enter user name:")
if user_name == name:
   print("Welcome to gmail: ", name)
else:
   print("Invalid user name, please try again")
   #An example of a string with space, .nb, a space is counted as a character in a print function. strip() help to remove the space.
   course = "Python  "
print("with spaces course length is: ",len(course))
x=course.strip()
print("after removing spaces, course length is: ",len(x))
#How to changes cases strings in Python. Example below
message='Python programming language'
print(message.upper()) # This method converts all characters into upper case
print(message.lower()) #This method converts all characters into lower case
print(message.swapcase())#This method converts all lower-case characters to uppercase and all upper-case characters to lowercase
print(message.title())# The first character in every word will be in upper case and all remaining characters will be in lower case
print(message.capitalize())# Only the first character will be converted to upper case and all remaining characters can be converted to lowercase.
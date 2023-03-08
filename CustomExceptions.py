# class NegativeError(Exception):
#    def __init__(self, data):
#        self.data = data

# try:
#    x = int(input("Enter a number between positive integer: "))
#    if x < 0:
#       raise NegativeError(x)
#    else:
#       print(" You have entered a correct number ")
# except NegativeError as e:
#    print("You provided {}. Please provide positive integer values only".format(e))

# """Example 2"""
class TooYoungException(Exception):
   def __init__(self, arg):
       self.msg=arg
class TooOldException(Exception):
   def __init__(self, arg):
       self.msg=arg

age=int(input("Enter Age:"))
if age>60:
   raise TooOldException("Your age already crossed marriage age...no chance of getting marriage")
elif age<18:
   raise TooYoungException("Plz wait some more time you will get best match soon!!!")
else:
       print("You will get match details soon by email!!!")
"""READING AND LATER WRITING OTHER EXTERNAL FILES."""
   # TOPIC 1. READING FROM FILES
y= open("Rev23.txt" , "r")
"""Depending on your needs, you can use either of the below print functions"""
print(y.readable()) #Can/Will print a bool value, ie True or False depending on whether the file has any text
print(y.readline()) #This line will read an individual line
print(y.readlines())#This line will read all lines in an array ie a list.
print(y.readlines()[1]) # This can read the first line index in the file
print(y.read())# This line will read an entire file as it is 
y.close() #Whenever you open a file, you must close it. so this line is just for closing,
 #Nb, on the above example above ; we can also use for loop to iterate the file.
"""ie """
y= open('Rev23.txt' , 'r')
print(y.readable())
for employee in y.readlines():
   print(employee)
y.close()

 #However, a built in method called with is used to implicitly open and automatically close the file.eg  below
with open ("Rev23.txt" , "r") as emp:
   print(emp.readable())
   print(emp.read()) #other methods as above can be used

    #TOPIC 2. WRITING AND APPENDING FILES  ON EXTERNAL FILES IN PYTHON.
""" We look at writing new files, and appending on existing files"""
   #The main difference is on the choice of mode, ie read- "r" or r+, write -"w" or "w+", and append -"a" or "a+" modes.
#WRITING AND APPENDING FILES   IN PYTHON.
with open ("Rev23.txt" , "a") as emp:
   print(emp.write(" G- Great")) # we want to append F- Father to the exsternal file.
   #Know when to use a,a+. Or w,w+, or r,r+.
   print(emp.write("\n H- Honest")) #A special character \n  called an escape character can be used anywhere in the print function for a new line.
#NB, We can also write entirely create new files , with mode being w+

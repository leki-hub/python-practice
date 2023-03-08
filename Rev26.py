#WRITING AND APPENDING FILES  ON EXTERNAL FILES IN PYTHON.
with open ("Rev23.txt" , "a") as emp:
   print(emp.write(" G- Great")) # we want to append F- Father to the exsternal file.
   #Know when to use a,a+. Or w,w+, or r,r+.
   print(emp.write("\n H- Honest")) #A special character \n  called an escape character can be used anywhere in the print function for a new line.

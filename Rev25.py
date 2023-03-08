with open ("Rev23.txt" , "r") as emp:
   print(emp.readable())
   print(emp.readline()[1])

   print(emp.read())# is the same as print(emp.readlines)
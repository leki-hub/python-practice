d={}
n=int(input("Enter number of employees: "))
i=1
while i <=n:
   name=input("Enter Employee Name: ")
   salary=input("Enter Employee salary: ")
   d[name]=salary
   i=i+1

for x in d:
   print("The name is: ", x ," and his salary is: ", d[x])
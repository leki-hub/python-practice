rows = range(1, 5)
for x in rows:
   for stars in range(1, x+1):
    print('*' , end= ' ')
print()
#Example 
for i in range(0,4):
 for j in range(0,3):
   print(i,j)
  #Example 
  
num = int(input("Enter a number:"))
print(f"The entered the number is {num}")
ij=0,0
for i in range(0, num): 
  print() 
  for j in range(0,i+1): 
         print("+", end="")

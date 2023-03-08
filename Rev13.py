#break statements in python
for val in "MRCETC OLLEGE":
  if val == " ":
   break
  print(val)
print("The end")
  #Example 2
for num in [11, 9, 88, 10, 90, 3, 19]:
 print(num)
 if(num==88):
  
  print("The number 88 is found")
  print("Terminating the loop")
  break
 """ the above  is the same as """
for num in [11, 9, 88, 10, 90, 3, 19]:
 print(num)
 if(num==88):
   break
 print("The number 88 is found")
 print("Terminating the loop")

#Continue statements in python.
for val in "string":
 if val == "i":
  continue
 print(val)
print("The end")
#Pass statement in python
sequence= {"S", "p", "2", "we"} 
for items in sequence:
 pass  # in this line,is like saying a= None #In Python programming, pass is a null statement. It is included when there is no action needed on syntax. its passed to avoid an error







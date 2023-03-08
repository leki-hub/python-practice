item_costs = [10, 20, 30] #This is a list
sum=0 # intialization
for x in item_costs:
   sum=sum + x
   print(sum)
#Example 2
x = [10, 20, 30, "Python"]
for i in x:
  print(i)
#Example 3
x= "python"
for s in x:
 print(s)
 #The below example is a nested loop, /ie a loop inside the other
rows = range(1, 5)
for x in rows:
for star in range(1, x+1):
print('* ', end=' ')
   #print()
   #Create a simple for loop that multiplies the values in a range
for i in range(1,4):
    for j in range(1,4):
        print(i*j)
        #A simple program that creates a multiplication table of values between 1 and 10
for i in range(1,11):
    for j in range(1,11):
        print(i*j , end ="\t")
    print()
    #check this example that multplies numbers from 1 to 3
for i in range(1, 4):
    for j in range(1, 4):
        print(i, "*", j, "=", i*j)
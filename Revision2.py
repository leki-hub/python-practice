sum = 0
num = int(input("Enter  the  highetst number  : "))
i=1
while i <= num:
      if i % 2 == 0:

        sum +=i
      i+=1
print("The sum of even numbers to" , num , "is " ,sum)
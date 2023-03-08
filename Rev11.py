#Write a program to display mrecet cse dept 10 times on the screen.using while loop

def usingFunctions():
 count =0
 while count<10:
    print("mrcet cse dept",count)
  
    count=count+1
  
usingFunctions()
"""or """
count =0
while count<10:
    print("mrcet cse dept",count)
  
    count=count+1
"""USING FOR LOOP"""
def to_count():
    i=1
    for i in range(1,10):
     print(" mrcet cse dept " , i)
    i+=1
to_count()
"""Or"""
i=1
for i in range(1,10):
    print(" mrcet cse dept " , i)
    i+=1
     ### Can also be simply written as below, meaning that its not neccesary to initialize in for loop, but neccesary in while loop
for i in range(2,10):
    print(" mrcet cse dept " , i)
#1 Factorial: syntax happens as below
    #factorial(3) = 3 * factorial(2)
    #factorial(2) = 3 * 2 * factorial(1)
    #factorial(1) = 3* 2 * 1 * factorial(0)
    #factorial(n) = n * factorial(n-1)
#Example.
def f1():
   n=4
   fact=1
   while(n>0):
       fact=fact*n
       n=n-1
   print("Factorial of the number is: ", fact)

f1()
"""Example 3"""
def fun(n,res=1):

   if(n<=0):

       return res

   return fun(n-1,n*res)

print(fun(5))
#or
def fun(n,res=1):

   if(n>0):#This is for setting recursion limit.
   
      return fun(n-1,n*res)
   else:
      return res

print(fun(5))
#or
def factorial(n):
    if n == 0:
        return 1
    else:
         return n * factorial(n-1) #= n *factorial(n-1) =n*(n-1) *(n-2)*(n-3)... 1. 
print(factorial(5))
"""Example 2"""
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
print(factorial(5))
#Topic ;Factorial and recursions.This example is for factorial
# def  iterativeFactorial(n):
#     result= 1 
#     for i in range(n,0,-1): # this is to say from  from range 5 to 0 but in a negative steps.
#       result= result*i
#     return result
    
# print(iterativeFactorial(7))
# exit() # This is optional since the program will exit upon executing the above commands

def fibonacci(n):
 if n<=1:
   return n
 else:  
  return fibonacci(n-1) + fibonacci(n-2)
     
print(fibonacci(6))

def fibonacci(n):
    """Returns the first n Fibonacci numbers"""
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_fib = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(next_fib)
    return fib_sequence[:n]
print(fibonacci(6))
# y= [1, 2]
# s= [3,4]
# print(y+s)
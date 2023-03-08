x= 10 #this is a global variable, ie is in a global scope
def afuntion():
    x=20 #this is a local variable, ie is in a local scope.
afuntion()
print(x)
#however, running the above program will print 10, and not 20, thus whenever we want to refer to a global variable inside a function, we add global then leave a  space and write the varable as below
x= 10
def afuntion():
     global x
     x=20
afuntion()
print(x) #the output here will be 20 and not ten
#Example 3
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
#example 4. /In the below example, the 2 print executions will be done both localy and then globally
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

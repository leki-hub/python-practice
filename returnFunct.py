#Leaning about the return function
def m1(a, b):
   c = a+b
   d = a-b
   return c, d
#calling function
x, y = m1(10, 5)
print("sum of a and b: ", x)
print("subtraction of a and b: ", y)
# Another example
def sum(a, b): # defining a function
  print("Sum of two numbers is: ", (a+b))
sum(3,4)
#different approach 
def sum(a, b): # defining a function
   c = a + b
   return c
x=sum(3, 4)
print("Sum of two numbers is: ",x)
#/ NB , if there is no return statement in the function body, then the function by default returns  : None
#Calling a function without placing objects inside the brackets means that the output is also :None ie /you must tell it the object/s to be acted on.
 #EXAMPLE 3. How to return more than 1 variable , example below.
def m1(a, b):
   c = a+b
   d = a-b
   return c, d
#calling function
x, y = m1(10, 5)
print("sum of a and b: ", x)
print("subtraction of a and b: ", y)
#Using keys in a user defined function example on keys and arguements
def cart(item, price):
   print(item, "cost is :" ,price)

cart(item="bangles", price=20000)
cart(item="handbag", price=100000)
cart(price=1200, item="shirt")
     #Example 2  possible scenarios, using keys and arguements
def details(id, name): 
    print("Emp id is: ",id)
    print("Emp name is: ",name)

# calling function
details(1, name="Anushka") # nb, the key 1 should come befor the arguement 'name'.
     #Example 3  , possible scenario
def details(id, name):
    print("Emp id is: ",id)
    print("Emp name is: ",name)

# calling function
details(id=1, name="Balayya Babu")
details(id=2, name="Chiru")
# Another simple example
def sub(x, y):
   print(x-y)
# calling function
sub(10, 20)
   #Example 4(1).  / Check notes about variable length. Nb, the essense of *y is used to mean the length of a formal arguement x.
            # we use *y if not sure the number of variable we might need to call later.This gives room to infine x varaibles being called .
def total_cost(x, *y): # X is a variable. *y is an open length number.
   sum=0
   for i in y:
       sum+=i
   print(x + sum)

#calling function
total_cost(100, 200) #valid
total_cost(110, 226, 311) #valid
total_cost(11,) #valid
  #Example 4(2) / *args " allows a function to accept any number of positional arguments, and they are passed to the function as a tuple. , while 
                  # **kwargs" allows a function to accept any number of keyword arguments, and they are passed to the function as a dictionary.
def my_function(*m, **kwargs): #row63 nb *m ,64,65 executes the variable-length argument
    for x in m:
        print(x)
    for key, value in kwargs.items(): #row63,66,67, and the key parts nb , from ,name= .... in row  69
        print(key, ":", value)

my_function(1, 2, 3, name="John", age=25)
 #Example 4(2) keyword variable-length in python.. 
 #          **x allows a function to accept any number of keyword arguments, and they are passed to the function as a dictionary.
def m1(**x):
   for k, v in x.items():
       print(k,"=",v)

m1(a=10, b=20, c=30)
m1(id=100, name="Subbalaxmi")
   #Example 4 (3)
def print_kwargs(**sam):
   print(sam)

print_kwargs(id=1, name="Nireekshan", qualification="MCA")
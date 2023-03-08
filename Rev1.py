   #       TYPES OF Arguments
   # 1 Formal and informal variables.
def sum(a, b):#Nb a, b are just place holders for variables that shall later be declared in the program
   c = a + b            # a and b are formal arguments
   print(c)
# call the function
x = 10
y = 15
sum(x, y)            # x and y are actual arguments
#Example 2
def sub(x, y):
  print(x-y)
#calling function
sub(10, 20)
 #Example 3
def add_numbers(a, b): #Nb a, b are just place holders for variables that shall later be declared in the program
    result = a + b #By Using an expression on arguements, you must use result statement to prompt the program to recognize that expression, otherwise, the output at console will be : None. nb , you always must use print function to display 
    return result
sum = add_numbers(3, 5)
print(sum)
# 2 Keyword Arguments.
   #example 1
def cart(item, price): # item is the key, ie a key is just a nme of the variable.
   print(item, "cost is :" ,price)# The keyword should start , then the object word. ie at the print function, it should start with a keyword then the object

cart(item="bangles", price=20000)
cart(item="handbag", price=100000)
cart(price=1200, item="shirt")# nb the change of order here does not affect output. ie no effect on what to start with  while calling calling
  #Example 3
def details(id, name):
    print("Emp id is: ",id)
    print("Emp name is: ",name)

# calling function
details(id=1, name="Balayya Babu")
details(id=2, name="Chiru")
 #Example 4
def details(id, name):
    print("Emp id is: ",id)
    print("Emp name is: ",name)

# calling function
details(1, name="Anushka")
   #DEFAULT ARGUMENTSS
  #    NB , In the function definition, while declaring parameters, we can assign some value to the parameters, which are called default values. Such default values will be considered when the function call does not send any data to the parameter.
     #Example 1
def cart(item, price=20): #price is default
   print(item, "cost is :" ,price)

cart(item="pen")
cart(item="handbag", price=10000)
cart(price=500, item="shirt")
 #NB , In the above syntax, the daefault variable is the one not specified in the call function but is declared in call function name.
   # Example 1.1 below will thus give an error  because While defining a function, after default arguments we should not take non-default arguments.
def cart(item, price=1): #item is default
   print(item, "cost is :" ,price)

cart(item="pen")
cart(item="handbag", price=10000)
cart(price=500, item="shirt")
 # 3 VARIABLE ARGUMENT LENGTH (*variable) in Python:
  #Sometimes, the programmer does not know how many values need to pass to function. In that case, the programmer cannot decide how many arguments to be given in the function definition.
  #The variable-length argument is written with a ‘*’ (one star) before the variable in the function defintion.
      # / x is a formal argument, *y is a variable-length argument. Now we can pass any number of values to this *y. Internally the provided values will be represented in the tuple.
   #Example 1 below
def total_cost(x, *y): #y is a holder for any number of nonkeyworded variables.
   sum=0
   for i in y:
       sum+=i
   print(x + sum)

#calling function
total_cost(100, 200) #valid
total_cost(110, 226, 311) #valid
total_cost(11,) #valid
  #4 KEYWORD VARIABLE LENGTH ARGUMENT  (**variable) in Python: /describes arguments that are n key-value pairs.
   #Example 1 below.
def print_kwargs(**kwargs):
   print(kwargs)

print_kwargs(id=1, name="Nireekshan", qualification="MCA")
   #Example 2 belw.
#VARIABLE ARGUMENT LENGTH
  #IN Summary, check the below compressed syntax for both Variable-length and Keyword-variable length
def variable_args_function(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

variable_args_function(1, 2, 3, name="John", age=32)
     #NB, in the above syntax, the call function is the same but the console is different, thus *args will act on 1,2,3 , while  **args will  act on ; name="John", age=32.


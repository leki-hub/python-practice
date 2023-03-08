#Example 1(i)
def uppercase_decorator(func):
    def wrapper():
        func_result = func()
        return func_result.upper()
    return wrapper

@uppercase_decorator
def greet():
    return "Hello, World!"

print(greet())
 #Example 1(ii)- a bit similar
def uppercase_decorator(func):
    def wrapper():
        func_result = func()
        return func_result.upper()
    return wrapper

@uppercase_decorator
def greet():
    return "Hello, World!"

print(greet())
#Example 2
def decor(func):
   def inner_function(x,y):
       if x<0:
           x = 0
       if y<0:
           y = 0
       return func(x,y)
   return inner_function 

@decor
def sub(a,b):
   res = a - b
   return res

print(sub(30,20))
print(sub(10,-5))
"""Example- yet to practice """
def retry_decorator(max_retries):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Retrying {func.__name__} ({i+1}/{max_retries}) after error: {str(e)}")
            raise Exception(f"Failed to execute {func.__name__} after {max_retries} retries.")
        return wrapper
    return decorator

@retry_decorator(max_retries=3)
def divide(a, b):
    return a / b

print(divide(10, 2))
print(divide(5, 0))

"""Example """
""" Understanding how decorators work """
def decorator_function(originalfunction):
    def wrapper_function(*args,**kwargs):
      print(f"The wrapper executed this before calling the display functio {originalfunction. __name__}")
      return originalfunction(*args,**kwargs)
    return wrapper_function

# def display():
#    print("This is a decorated function")
# assigndecoratedas= decorator_function(display)#Here , we've set a variable assigndecoratedas to hold what the outer function does when the inner function is passed to it.
# assigndecoratedas()
         #Decorator functions helps us add more functionalties/manipulation to the wrapper funtion without having to tamper with the original decorated function,as in line
"""Instead of using line8- line 11, we can simly use a @decoratorfunction name above the display function as below"""
@decorator_function
def display():
    print("This is a decorated function")

@decorator_function
def display_info(name,age):
   print(f"The name of the person is {name} and the age is {age}")
display_info("John",45)
display()
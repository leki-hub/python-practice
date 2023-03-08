"""Decorators in Python """
 #Example 1
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
def square_decorator(func):
    def wrapper(x):
        result = func(x)
        return result * result
    return wrapper

@square_decorator
def double(x):
    return x * 2

print(double(5))
#Example 3.
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Something is happening before the function is called.
# Hello!
# Something is happening after the function is called.


#We can create two (or more) functions where the output of one function is the input for another
def add(x):
    return x *2

def square(x):
    return x * x

def composed_function(x):
    return square(add(x))

result = composed_function(5)
print(result)

"""An example of functions composition , nb -represented as g(f(x))"""
def f(x):
 return 0 if x == 0 else 2 * f(x - 1) + x

def g(x):
        return sum(f(i) for i in range(x + 1))

print(g(2))
print(f(2))
#is the same as ;
def g(x):
        return sum(f(i) for i in range(x + 1))
def f(x):
 return 0 if x == 0 else 2 * f(x - 1) + x

print(f(2))
print(g(2))
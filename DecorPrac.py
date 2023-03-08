def myfunc(f1):
    def wrapper(*args, **kwargs):
        print("Extra functionality")
        s= f1(*args, **kwargs)
        print("was printed as above")
        return s*s
    return wrapper
# x= myfunc("Hello")
# print(x)
# x()
@myfunc
def f2(x ,y):
     print("The function to manipulate wrapper" , x ,y)
     return y
# @myfunc    
# def f3(x,y):
#  print("Func3" ,x,y)
# # f2= myfunc(f2)   
# # f3= myfunc(f3)
x = f2(5, 6)
print(x)
# f3(3,9)
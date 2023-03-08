a= int(input("Enter value a : "))
b = int(input("Enter value b : "))
def calculate(a,b):
   sum=  a+b
   diff= a-b
   prod= a*b
   div=a/b
   mod= a%b
   exp= a**b
   return sum,diff,prod,div,mod,exp

p,q,r,s,t,u= calculate(a,b)
print("sum = ", p, "diff= " ,q, " prod = " ,r, "div= ", s, "mod = " , t, " exp= ", u)
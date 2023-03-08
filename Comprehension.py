#1 TUPLE COMPREHENSION. Nb , The result of a tuple comprehension is special. You might expect it to produce a tuple, but what it does is produce a special "generator" object that we can iterate over.
 # Example1  below.
x = (i for i in 'abc') ;"""This is a tuple """
print(x)
"""We can now iterate the generator using for loop""" #NB, The iteration in tuple is only done once
for i in x:
    print(i)
  #Example 2, Create a list of 2-tuples like (number, square):
s = ((x,x**2 )for x in range(6))
print(s)
"""We can now iterate the generator using for loop"""
for i in s: 
  print(i, end= "")
# 2- SET COMPREHENSION.
   #Example below
a = {x for x in 'abracadabra' if x not in 'abc'}; """This is to say, get elements in abracadabra, excluding elements a, b, and c if found"""
    #Example 2 
s={3*x for x in range(10) } ; """ also check x={3*x for x in range(10) if x>5}"""
print(s)

#LISTS COMPREHENSION. 
 #Example below
squared_numbers = [x**2 for x in range(10)] #All values will be printed in the iterable since there is no condition set.
print(squared_numbers)
#DICTIONARY COMPREHENSION.-A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.
  #syntax is as shown below
X={1:'A',2:'B',3:'c'}
y= dict([('a',3) ,('b',4)]) #This aplies the dctionary constructor using casting
 #Example 1 below
z={x: x**2 for x in (2,4,6)}
print(z)
 #Example 2
dict11 = {x: x*x for x in range(6)}
  #Example 3
dict1 = {"brand":"mrcet","model":"college","year":2004}
print(dict1)
"""Iterating over (key, value) pairs:"""
     #Example 4(i)below
x = {1:1, 2:4, 3:9, 4:16, 5:25}
for s in x:
    print(s, x[s])
    # Altenatively iterating through , example 4(ii) below- 
for k,v in x.items():
 print(k,v)
  



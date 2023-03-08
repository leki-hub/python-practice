"""cmp special function""" #THe cmp function is from word compare, thus  used to compare tuples and return True or False.
def cmp(t1, t2):
  
     return bool(t1>t2) - bool(t1 < t2)
def cmp(t3, t4):
   return bool(t3 > t4) - bool(t3 <t4)
def cmp(t5, t6):
   return bool(t5> t6) - bool(t5 < t6)
t1 = (1,3,5) # Here t1 is lower than t2, since the output is -1
t2 = (2,4,6)

t3 = (5)#Here t3 is higher than t4 since the output is 1
t4 =(4)

t5 = (3.14,) #Here t5 is equal  to t6 since the output is 0
t6 = (3.14,)

print(cmp(t1, t2))
print(cmp(t3, t4))
print(cmp(t5, t6))
nested_tuple =("biotechnology,", (0,5),('fermentation', 'ethanol'), (3.14, 'pi, 1.618, 'golden ratio,'))
nested_tuple
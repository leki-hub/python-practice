def myfunct(list):
    for i in range(len(list)):
      list[i] *=2
      return[i for i in list if i%4 ==0] #item to be returned is a comprehension with given condition
print(myfunct([1,2,4,8,10,12]))
"""or """
list= [1,2,4,8,10,12]
def myfunct(list):
    for i in range(len(list)):
      list[i] *=2
      return[i for i in list if i%4 ==0] #item to be returned is a comprehension with given condition
print(myfunct(list))
"""or """
list= [1,2,4,8,10,12]
for i in range(len(list)):
      list[i] *=2
      print(i)
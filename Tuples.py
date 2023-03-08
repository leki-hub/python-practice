#Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created. However, you can change first to a list in order to make it mutable
   # Example. To add, you can convert to list and use : 1 append() -check w3s, or alternatively like below where IT IS ONLY POSSIBLE TO ADD A TUPLE TO A TUPLE as in example below
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)
# Looping through a tuple, example below
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
  #Example 2
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
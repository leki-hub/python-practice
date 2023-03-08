 # how to Unpack a collection./ python allows variables to be assigned on items in the list or tuple
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

print(x)
print(y)
print(z)
#Unpack a collection example 2

Lessons= [ "Maths ", "English", "Geog" ]
morning, afternoon, evening= Lessons

print(morning, evening, afternoon)
#you can also use + instead of a comma operator to output several string variables. you cannot hower add an integer type and a string type
print(morning + afternoon + evening)

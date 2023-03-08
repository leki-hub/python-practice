# LAMBDA FUCTIONS IN PYTHON.-Function: A lambda function is an anonymous function that is defined without a name.
                           # It is defined using the "lambda" keyword followed by a set of parameters, a colon, and an expression.
                           #...The expression is evaluated and returned when the function is called. Lambda functions are used to write small, one-time use function
 #NB; the lambda syntax is like ; lambda argument_list: expression
 #NB -A lambda function can take any number of arguments but should have only one expression.
#Example 1 below.
s = lambda a: a*a
x=s(4)
print(x)
#Example 2 below.
add = lambda a,b: a+b
x=add(4,5)
print(x)
 #SUB TOPIC- FILTER , REDUCE, MAP fuctinons.
#The lambda function, mostly, can be used in combination with other functions such as map(), reduce(), filter() .
  #filter()-This function is used to filter values from a sequence of values.
  #map()-This function is used to map a particular function onto the sequence of elements.
  #reduce()- This function reduces the sequence of elements into a single element by applying a specific condition or logic.
#A combined example below.
numbers = [1, 2, 3, 4]

# using filter
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# using reduce
from functools import reduce # Nb, to use reduce function, we must import functools module
sum_of_numbers = reduce(lambda x, y: x + y, numbers)

# using map
squared_numbers = list(map(lambda x: x**2, numbers))
#Other examples below.
 #Example on filter() function
items_cost = [999, 888, 1100, 1200, 1300, 777]
gt_thousand = filter(lambda x : x>1000, items_cost)
x=list(gt_thousand)
print("Eligible for discount: ",x)
#Example on map() function
without_gst_cost = [100, 200, 300, 400]
with_gst_cost = map(lambda x: x+10, without_gst_cost)
x=list(with_gst_cost)
print("Without GST items costs: ",without_gst_cost)
print("With GST items costs: ",x)
#Example on reduce() function
from functools import reduce
each_items_costs = [111, 222, 333, 444]
total_cost = reduce(lambda x, y: x+y, each_items_costs)
print(total_cost)
"""Lambda example"""
y = 8
z = lambda x : x * y
print (z(6))
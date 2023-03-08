# Generators are just like functions which give us a sequence of values one as an iterable
# Generators contain yield statements just as functions contain return statements
 #Example1 .
def m():
   yield 'Mahesh'
   yield 'Suresh'

g = m()
print(g)
print(type(g))
for y in g:
   print(y)
   #Example 2.
def m(x, y):
   while x<=y:
       yield x
       x+=1

g = m(5, 10)
for y in g:
   print(y)
  # next function in Python:
      #If we want to retrieve elements from a generator, we can use the next function on the iterator returned by the generator.
      #Apart fro looping, This is the other way of getting the elements from the generator.
"""The next function can supplement the yield function, when no either for or while looping is used, ie the next() function lazily calls the next item that was to be displayed/returned """
#Example 3.0  below.-in case of example 1 above
"""An example below """
def m():
   yield 'Mahesh'
   yield 'Suresh'
g = m()

print(type(g))
print(next(g))
print(next(g))
   #Example 3.1
def even_numbers():
    num = 0
    while num < 10:
        yield num
        num += 2
gen = even_numbers()
print(next(gen)) # Output: 0
print(next(gen)) # Output: 2
print(next(gen)) # Output: 4
print(next(gen)) # Output: 6
print(next(gen)) # Output: 8
"""Once the generator has generated all the values in the sequence,""",
"""it will raise a StopIteration exception. """
"""You can catch this exception to gracefully handle the end of the sequence:"""
 #Thus alternatively; the below program will handle the error when iteration stops.
def even_numbers():
    num = 0
    while num < 10:
        yield num
        num += 2
gen = even_numbers()
try:
    while True:
        print(next(gen))
except StopIteration:
    print("Sequence ended.")


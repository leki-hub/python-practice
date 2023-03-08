#The __iter__() method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself."""
#The __next__() method also allows you to do operations, and must return the next item in the sequence."""
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
"""We need to stop the iteration, by raising StopIteration exception"""
#To prevent the iteration to go on forever, we can use the StopIteration statement.
  #On the above example, 
"""In the __next__() method, we can add a terminating condition to raise an error if the iteration is done a specified number of times:"""
     #ie, stop after 20 iterations.
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)
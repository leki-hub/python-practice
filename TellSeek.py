f=open("mytext.txt", 'w')
list=["Ramesh\n" ,"Arjun\n", "Senthil\n", "Vignesh"]
f.writelines(list)
print("List of lines written to the file successfully")
f.close()
print(f.closed)
with open("mytext.txt", 'r') as s:

 print(s.read())
 y= s.readlines()
#  print(s.readline())
#  print(s.readline())
# print(s)
for line in y:
   print(line , end="")
"""Tell and seek methods """
"""#We can use the tell() method
    to return the current position of the cursor(file pointer) from the beginning of the file. 
    The position(index) of the first character in files starts from zero just like string index."""
#Example
# Opening a file in read mode
with open("mytext.txt", "a") as r:

  print(r.readline()) # Reading the first line of the file
  print(r.readline())
  print(r.readline())
  print(r.tell())

position = r.tell() # Getting the current position of the file pointer
shift= r.seek(17)
print(position)
print(shift)
print(r.write("I can"))
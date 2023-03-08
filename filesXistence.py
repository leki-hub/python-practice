import os, sys
fname=input("Enter File Name: ")
if os.path.isfile(fname):
   print("File exists:", fname)
   f=open(fname, "r+")
else:
   print("File does not exist:", fname)
   sys.exit(0)
print("The content of file is:")
data=f.read()
print(data)

"""Program to print the number of lines, words and characters present in the given file"""
#Example
import os, sys
fname=input("Enter File Name: ")
if os.path.isfile(fname):
   print("File exists:", fname)
   f=open(fname, "r")
   # print(f.read())
else:
   print("File does not exist:", fname)
   sys.exit(0)
# f=open(fname, "r")
lcount=wcount=ccount=0
for line in f:
   lcount=lcount+1
   ccount=ccount+len(line)
   words=line.split()
   wcount=wcount+len(words)
print("The number of Lines:", lcount)
print("The number of Words:", wcount)
print("The number of Characters:", ccount)

"""Zipping files, where 2 or more files are zipped into binary data where decoding requires special editors"""
  #Example 
from zipfile import *
f=ZipFile("files.zip", 'w', ZIP_DEFLATED)
f.write("sample_log.txt")
f.write("thor.jpeg")
f.close()
print("files.zip file created successfully")
"""Or alternatively also;"""
import zipfile

with zipfile.ZipFile('my_archive.zip', 'w') as zip:
    zip.write('file1.txt')
    zip.write('file2.txt')

"""Unzipping files- To perform unzip operation in Python:""" 
#We need to create an object in the same way as we did for zipping the file. But the argument values here are different.
   # NB , Once we created ZipFile object for unzip operation, we can get all file names present in that zip file by using namelist() method
from zipfile import *
f=ZipFile("files.zip", 'r', ZIP_STORED)
names=f.namelist()
for name in names:
   print( "File Name: ",name)

   """Or alternatively also, """
import zipfile

with zipfile.ZipFile('my_archive.zip', 'r') as zip:
    for name in zip.namelist():
        print(name)

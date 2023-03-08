#Usually a programmer should take very much care to create objects, and sometimes he may neglect destruction of useless objects.
#Due to this negligence, at a certain point of time there may be a chance, total memory can be filled with useless objects which creates memory problems and total application will be down with Out of memory error.
#But in Python, internally a program will run in background always to destroy useless objects.
#So, the chance of failing a Python program with memory problems are very little.
      #The above  program is nothing but Garbage Collector.
#The main objective of Garbage Collector is to destroy useless objects. If an object does not have any reference variable, then that object is eligible for Garbage Collection.
#By default, the Garbage collector is enabled, but we can disable it based on our requirement. 
   # In order to do so, we need to import the gc module. 
#as below
   #gc.isenabled() – This method returns True if garbage collector is enabled
   #gc.disable() – This function is used to is disable the garbage collector explicitly
   #gc.enable() – This function is used to is enable the garbage collector explicitly
#Syntax example below.
import gc
print(gc.isenabled())
gc.disable()
print(gc.isdisebled())
gc.enable()
print(gc.isenabled())
"""How to check/know the currernt thread being used"""
import threading
print("Current Executing Thread:",threading.current_thread().getName())
   #There are two ways in which we can create a thread in python. They are as follows:
"""1 Creating a Thread with pre-defined ‘Thread’ class""" #2 Creating a our own thread class by inheriting Thread class
from threading import *
def display():
   for i in range(6):
       print("Child Thread")
t=Thread(target=display)
t.start()
for i in range(6):
   print("Main Thread")

#Example 2- to control the number of threads, and control execution order, we include  locks and semaphores in our syntax,-Check chatGPT 
from threading import *
class Demo:
   def display(self):
       for i in range(6):
           print("Child Thread")
obj=Demo()
t=Thread(target=obj.display)
t.start()
for i in range(6):
   print("Main Thread")
    #How to use "Locks" and "semaphores" on the above example- check ChaGPT for elaboration
import threading

class Demo:
    def __init__(self):
        self.lock = threading.Lock()
        self.semaphore = threading.Semaphore(1)

    def display(self):
        with self.lock:
            for i in range(6):
                print("Child Thread")
                self.semaphore.release()

    def main(self):
        for i in range(6):
            self.semaphore.acquire()
            print("Main Thread")
        t.join()

obj = Demo()
t = threading.Thread(target=obj.display)
t.start()
obj.main()
"""2 Creating a our own thread class by inheriting Thread class """ 
#Example 1- check how to include the use of Lock and Semaphore in chatGPT 
from threading import *

class MyThread(Thread):
   def run(self):
       for i in range(6):
           print("Child Thread")
t=MyThread()
t.start()
for i in range(6):
   print("Main Thread")
#Example 2
from threading import *
import time
def divison(numbers):
   for n in numbers:
       time.sleep(1)
       print("Double:", n/5)

def multiplication(numbers):
   for n in numbers:
       time.sleep(1)
       print("Square:", n*5)
numbers=[10,20,30,40,50]
begintime=time.time()
divison(numbers)
multiplication(numbers)
print("The total time taken:", time.time()-begintime)

#Example

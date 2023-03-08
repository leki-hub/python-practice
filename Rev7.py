import threading
import time
class MyThread(threading.Thread):
    def __init__(self, thread_id, name, delay, lock, semaphore):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.delay = delay
        self.lock = lock
        self.semaphore = semaphore

    def run(self):
        print(f"Starting thread {self.thread_id} ({self.name})")
        with self.lock:
            print(f"Thread {self.thread_id} ({self.name}) has acquired the lock")
            for i in range(5):
                with self.semaphore:
                    print(f"Thread {self.thread_id} ({self.name}) counting: {i+1}")
                    time.sleep(self.delay)
            print(f"Thread {self.thread_id} ({self.name}) is releasing the lock")
        print(f"Exiting thread {self.thread_id} ({self.name})")

# Create a Lock and a Semaphore object
lock = threading.Lock()
semaphore = threading.Semaphore(2)  # Only allow 2 threads to access the shared resource at once

# Create and start multiple instances of MyThread
thread1 = MyThread(1, "Thread 1", 1, lock, semaphore)
thread2 = MyThread(2, "Thread 2", 2, lock, semaphore)
thread3 = MyThread(3, "Thread 3", 3, lock, semaphore)

thread1.start()
thread2.start()
thread3.start()

# Wait for all threads to finish
thread1.join()
thread2.join()
thread3.join()

print("All threads have finished")


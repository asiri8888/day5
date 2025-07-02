import time
import threading
def long_task():
    print("Long tasks: Starting....(this will take 3 seconds)")
    time.sleep(3) # Simulating a 6 second wait
    print("Long tasks: Finished after 6 seconds")


def short_task():
    print("Short tasks: Starting....(this will take 1 second)")
    time.sleep(0.5) # Simulating a 1 second wait
    print("Short tasks: Finished ")

print("program without threads")
short_task() # run short thask first
long_task() # run long task second (program will pause here for 3 seconds)
short_task() # run short task again (program will pause here for 0.5 seconds)
print("program with threads")

# Create threads for long  tasks
background_thread = threading.Thread(target=long_task)

# Start the new thread. it begins running concurrently with the main thread
background_thread.start()

#meanwhile, the main thread can continue to run other tasks
short_task() # run short task first (program will pause here for 1 second)
short_task() # run short task again (program will pause here for 1 second)

#wait for the background thread to finish before exiting the main program
background_thread.join() # this will block the main thread until the background thread is done
print("program with threads finished")
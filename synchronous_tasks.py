import time
def long_task():
    print("Long tasks: Starting....(this will take 3 seconds)")
    time.sleep(6) # Simulating a 3 second wait
    print("Long tasks: Finished after 3 seconds")


def short_task():
    print("Short tasks: Starting....(this will take o.5 second)")
    time.sleep(1) # Simulating a .5 second wait
    print("Short tasks: Finished ")

print("program without threads")
short_task() # run short thask first
long_task() # run long task second (program will pause here for 3 seconds)
short_task() # run short task again (program will pause here for 0.5 seconds)
print("program without threads")
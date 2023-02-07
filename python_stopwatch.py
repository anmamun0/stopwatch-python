import time

start = time.time()
input("Press enter to stop the stopwatch: ")
stop = time.time()

elapsed_time = stop - start
print("Elapsed time: {:.2f} seconds".format(elapsed_time))

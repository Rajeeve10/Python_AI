import time


def display_time():
    epoch_time = time.time()
    readable_time = time.ctime(epoch_time)

    print("Seconds since epoch:", epoch_time)
    print("Current date and time:", readable_time)


display_time()
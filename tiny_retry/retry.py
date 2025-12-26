import time

def retry(func, *args, times=3, delay=0.0, exceptions=(Exception,), **kwargs):
    for attempt in range(times):
        func()
        time.sleep(delay)

import time

def retry(func, *args, tries=3, delay=0.0, exceptions=(Exception,), **kwargs):
    """
    Documentation for retry
    
    :param func: The function to be called and retried
    :param args: Any arguments for the function
    :param tries: The number of times the function to be tried
    :param delay: The delay between retries (in seconds)
    :param exceptions: The specific exceptions that trigger a retry
    :param kwargs: Any keyword arguments for the function

    This function returns the result of the function, if succesful. If not, it will raise the last exception it encountered.
    """
    if tries < 1:
        raise ValueError("Error: tries must be at least 1!")

    for attempt in range(tries):
        try:
            return func(*args, **kwargs)
        except exceptions as exception:
            if attempt == tries - 1:
                raise
            time.sleep(delay)
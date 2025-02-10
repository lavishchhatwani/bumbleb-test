import time
import functools
import tracemalloc

def execution_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        start_time = time.time()  # Start timing
        result = func(*args, **kwargs)
        end_time = time.time()  # End timing
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' executed in {execution_time:.6f} seconds")
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print(f"Function '{func.__name__} Current: {current / 10**6} MB, Peak: {peak / 10**6} MB")
        return result
    return wrapper


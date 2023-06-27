import time

def print_time_taken(func):
    def decorator():
        start_time = time.time()
        func()
        time_taken = time.time() - start_time
        print(f"{func.__name__} took {time_taken} seconds")
        
    # It's needed. Without it, there will be ERROR. 
    # TypeError: 'NoneType' object is not callable
    return decorator 

@print_time_taken
def first_function():
    time.sleep(1.4)

@print_time_taken
def second_function():
    time.sleep(2.6)

first_function()
second_function()
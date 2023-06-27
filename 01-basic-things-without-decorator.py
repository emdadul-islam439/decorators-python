import time

def first_function():
    time.sleep(1.4)
    
def second_function():
    time.sleep(2.6)
    

start_time = time.time()
first_function()
time_taken = time.time() - start_time
print(f"First function took {time_taken} seconds")

start_time = time.time()
second_function()
time_taken = time.time() - start_time
print(f"Second function took {time_taken} seconds")
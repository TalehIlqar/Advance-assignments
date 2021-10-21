import time
import threading
import random, string

start_time = time.perf_counter()

array = []

def random_letter_func():
    all_letters = string.ascii_uppercase
    ran_let = ''.join(random.choice(all_letters) for _ in range(3))
    array.append(ran_let)

for i in range(100000):
    random_letter_func()
    
    
inputletter = input('Please, enter any letter: ')

def letter_function():
    words = list(filter(lambda x: x[0] == inputletter.upper(), array))
    print(words)

thread = threading.Thread(target=letter_function)
thread.start()
thread.join()

end_time = time.perf_counter()

print(end_time-start_time)


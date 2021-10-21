import time
import multiprocessing
import random, string

start_time = time.perf_counter()

array = []

def random_letter_func():
    all_letters = string.ascii_lowercase
    ran_let = ''.join(random.choice(all_letters) for i in range(3))
    array.append(ran_let)

for i in range(100000):
    random_letter_func()

inputletter = input('Please, enter a letter:')

def letter_function():
    word3 = list(filter(lambda x: x[0] == inputletter.lower(), array))
    print(word3)

thread = multiprocessing.Process(target=letter_function)
thread.start()
thread.join()

end_time = time.perf_counter()

print(end_time-start_time)
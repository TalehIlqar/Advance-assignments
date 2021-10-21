import random
import math
import time
import threading

start_time = time.perf_counter()

l1 = []
l2 = []

def random_num():
    a = math.ceil(random.randint(0, 100000))
    l1.append(a)
    b = math.ceil(random.randint(0, 100000))
    l2.append(b)

for i in range(100000):
    random_num()

def sum_func():
    return sum(l1) + sum(l2)

for i in range(1):
    i = threading.Thread(target=sum_func)
    i.start()
    # time.sleep(1)
    i.join()
    
print(sum_func())




end_time = time.perf_counter()

print(end_time-start_time)

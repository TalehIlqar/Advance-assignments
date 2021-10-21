import time
import multiprocessing

start_time = time.perf_counter()

def sleep_one_sec():
    print("starting to sleep")
    time.sleep(1)
    print('finissh slep')
    
p1 = multiprocessing.Process(target=sleep_one_sec)

p1.start()

end_time = time.perf_counter()

print(f'{end_time - start_time}')

# import time
# import requests
# import concurrent.futures


# start_time = time.perf_counter()

# def download_image(index):
#     r = requests.get("https://picsum.photos/200/300")
#     with open(f"images/image_{index}.jpg", 'wb') as f:
#         f.write(r.content)
#     print(f"Image {index} downloaded.")

# with concurrent.futures.ProcessPoolExecutor() as executor:
#     processes = [executor.submit(download_image, i) for i in range(100)]
#     for process in concurrent.futures.as_completed(processes):
#         process.result()

# end_time = time.perf_counter()

# print(f"Total time taken: {round(end_time - start_time)} seconds.")
import threading
import time
from concurrent.futures import ThreadPoolExecutor
def func(seconds):

    time.sleep(seconds)
    print(f"Sleeping for {seconds}")


ti1 = time.perf_counter()
# t1 = threading.Thread(target=func, args=[4])
# t2 = threading.Thread(target=func, args=[5])
# t3 = threading.Thread(target=func, args=[6])
# t1.start()
# t2.start()
# t3.start()
#
# t1.join()
# t2.join()
# t3.join()

with ThreadPoolExecutor() as execute:
    future1 = execute.submit(func, 4)
    future2 = execute.submit(func, 5)
    future3 = execute.submit(func, 6)
    # future4 = execute.submit(func, 7)
    # results = execute.map(func, [4, 5, 6])
ti2 = time.perf_counter()
print(ti2 - ti1)

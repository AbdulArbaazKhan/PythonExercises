import functools
import time

@functools.lru_cache(maxsize=None)
def fx(n):
    time.sleep(3)
    return n*10

print(fx(20))
print("done for 20")
print(fx(10))
print("done for 15")
print(fx(5))
print("done for 5")
print(fx(20))
print("done for 20")
print(fx(10))
print("done for 15")
print(fx(5))
print("done for 5")

# Here it is memoize
#stores cache in memory (ram) while our program is running
#We can use when we have limited values to run
# use in database fetching
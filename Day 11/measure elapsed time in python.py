#Using time
import time

start = time.time()

print('Singh')

end = time.time()
print(end - start)

#Using timeit
from timeit import default_timer as timer

start = timer()

print('Singh')

end = timer()
print(end - start)

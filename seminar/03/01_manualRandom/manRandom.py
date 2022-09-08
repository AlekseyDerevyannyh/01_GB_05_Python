import time
from random import randint

arr = list()
for i in range(10):
    number = randint(1, 5)
    time.sleep(1)
    arr.append(int(str(time.time())[-number:]))
print(*arr)

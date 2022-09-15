from os import system
system('cls')

data = [x for x in range(10)]

res = list(filter(lambda x: not x % 2, data))
print(res)
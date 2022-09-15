from os import system
system('cls')

li = [x for x in range(1,20)]

li = list(map(lambda x: x + 10, li))
print(li)

data = list(map(int, input().split()))
print(data)
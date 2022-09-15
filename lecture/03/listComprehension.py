from os import system
system('cls')

def f(x):
	return x ** 3

list = [i for i in range(1, 10) if not i % 2]
print(list)
list = [(i, f(i)) for i in range(1, 10) if not i % 2]
print(list)
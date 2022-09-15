from os import system
system('cls')
sum = lambda x, y: x + y

def calc(op, a, b):
	print(op(a, b))
calc(sum, 4, 5)
calc(lambda x, y: x + y, 4, 5)
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.(Доп)
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

from os import system

def fibonacci (n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		fib_2 = 0
		fib_1 = 1
		fib = 0
		for i in range(2, n + 1):
			fib = fib_2 + fib_1
			fib_2 = fib_1
			fib_1 = fib
		return fib

system('cls')

k = int(input('Введите число k: '))

fib_list = [0]
if k == 0:
	print(fib_list)
	exit()

for i in range(1, abs(k) + 1):
	fib_list.insert(0, fibonacci(i) * (-1) ** (i + 1))
	fib_list.append(fibonacci(i))

print(f'k = {k}   =>   {fib_list}')

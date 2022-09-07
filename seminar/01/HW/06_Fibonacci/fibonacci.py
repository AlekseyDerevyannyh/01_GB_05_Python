# Требуется найти N-е число Фибоначчи.

from os import system
system('cls')

n = int(input('Введите N: '))

if n < 0:
	print('ОШИБКА! N должно быть больше 0!')
elif n == 0:
	print('F(0) = 0')
elif n == 1:
	print('F(1) = 1')
else:
	fibonacci = 0
	fibonacci_2 = 0
	fibonacci_1 = 1
	for i in range(1, n):
		fibonacci = fibonacci_1 + fibonacci_2
		fibonacci_2 = fibonacci_1
		fibonacci_1 = fibonacci
	print(f'F({n}) = {fibonacci}')

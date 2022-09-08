# Требуется найти наименьший натуральный делитель целого числа N, отличный от 1

from os import system

system('cls')

n = int(input('Введите число N: '))
if n < 2:
	print('ОШИБКА! N должно быть больше 1!')
	exit()

div = 0
for i in range(2, n + 1):
	if n % i == 0:
		div = i
		break
print(f'Наименьший натуральный делитель {n} = {div}')

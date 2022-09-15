# Задайте натуральное число N. Напишите программу, которая составит
# список простых множителей числа N.

from os import system

system('cls')

n = int(input('Введите число N: '))
if n < 2:
	print('ОШИБКА! Число N должно быть больше 1!')
	exit()
factor = []
i = 2
while i <= n:
	if n % i == 0:
		n //= i
		factor.append(i)
		i = 2
	else:
		i += 1

print(factor)

# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

from os import system

system('cls')

dec = int(input('Введите десятичное число: '))
i = dec
bin = ''
while i > 0:
	if i % 2 != 0:
		bin = '1' + bin
	else:
		bin = '0' + bin
	i //= 2

print(f'{dec} -> {bin}')
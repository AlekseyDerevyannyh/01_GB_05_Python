# Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

from os import system
system('cls')

dayNumber = int(input('Введите номер дня недели: '))
if dayNumber > 0 and dayNumber < 6:
	print(f'{dayNumber} -> нет')
elif dayNumber > 5 and dayNumber < 8:
	print(f'{dayNumber} -> да')
else:
	print('Такого дня недели не существует')

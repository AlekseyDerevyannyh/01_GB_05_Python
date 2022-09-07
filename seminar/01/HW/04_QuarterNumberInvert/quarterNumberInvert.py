# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

from os import system
system('cls')

quarter = int(input('Введите номер четверти: '))
if quarter == 1:
	print('1 -> (x > 0; y > 0)')
elif quarter == 2:
	print('2 -> (x < 0; y > 0)')
elif quarter == 3:
	print('3 -> (x < 0; y < 0)')
elif quarter == 4:
	print('4 -> (x > 0; y < 0)')
else:
	print('ОШИБКА! Некорректный ввод номера четверти!')

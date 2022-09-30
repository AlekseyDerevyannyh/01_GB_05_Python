# 2. Дано натуральное число N и последовательность из N элементов.
# Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и
# использовать циклы (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

from os import system

def subs (number):
	if number < 1:
		return ''
	else:
		result = input('Введите число последовательности: ')
		return subs(number - 1) + ' ' + result

system('cls')

number = int(input('Введите количество чисел последовательности: '))
if number < 2:
	print('Ошибка ввода!')
	exit()
print(subs(number))

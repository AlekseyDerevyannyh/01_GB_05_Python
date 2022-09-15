# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from os import system
from random import randint

def CoefListToStrPolynom (coefList):
	polynom = ''
	for i in range(len(coefList) - 1):
		if coefList[i] == 0:
			if coefList[i + 1] != 0:
				polynom = polynom + ' + '
		elif coefList[i] == 1:
			if coefList[i + 1] != 0:
				if len(coefList) - i - 1 == 1:
					polynom = polynom + f'x + '
				else:
					polynom = polynom + f'x^{len(coefList) - i - 1} + '
			else:
				if len(coefList) - i - 1 == 1:
					polynom = polynom + f'x'
				else:
					polynom = polynom + f'x^{len(coefList) - i - 1}'
		else:
			if coefList[i + 1] != 0:
				if len(coefList) - i - 1 == 1:
					polynom = polynom + f'{coefList[i]}*x + '
				else:
					polynom = polynom + f'{coefList[i]}*x^{len(coefList) - i - 1} + '
			else:
				if len(coefList) - i - 1 == 1:
					polynom = polynom + f'{coefList[i]}*x'
				else:
					polynom = polynom + f'{coefList[i]}*x^{len(coefList) - i - 1}'

	if coefList[-1] != 0:
		polynom = polynom + f'{coefList[-1]} = 0'
	else:
		polynom = polynom + ' = 0'
	return polynom


system('cls')

k = int(input('Введите число k: '))
if k < 1:
	print('ОШИБКА! Число k должно быть больше 0!')
	exit()
coefList1 = [randint(1, 100)]	# коэффициент старшего члена многочлена берём от 1
for i in range(1, k + 1):
	coefList1.append(randint(0, 100))
print(CoefListToStrPolynom(coefList1))

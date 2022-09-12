# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:

from os import system

system('cls')

a = int(input('Введите коэффициент А: '))
b = int(input('Введите коэффициент B: '))
c = int(input('Введите коэффициент C: '))

d = b ** 2 - 4 * a * c
if d > 0:
	x1 = ((-b) + d ** 0.5) / 2 * a
	x2 = ((-b) - d ** 0.5) / 2 * a
	print(round(x1, 3), round(x2, 3))
elif d == 0:
	x1 = (-b) / 2 * a
	print(x1)
else:
	print('корней нет')

# Требуется посчитать сумму целых чисел, расположенных между числами 1 и N включительно.

from os import system

system('cls')

n = int(input('Введите число N: '))
summ = 0
for i in range(1, n + 1):
	summ += i

print(f'Сумма равна: {summ}')

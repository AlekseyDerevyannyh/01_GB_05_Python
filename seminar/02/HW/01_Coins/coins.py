# На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток,
# которые нужно перевернуть, чтобы все монетки были повернуты
# вверх одной и той же стороной.

from os import system
from random import randint

system('cls')

n = int(input('Введите количество монеток на столе: '))
coins = []
count_0 = 0
count_1 = 0
for i in range(n):
	coins.append(randint(0, 1))		# формируем случайное расположение монет
	if coins[i]:
		count_1 += 1
	else:
		count_0 += 1

print(f'Монетки лежат следующим образом: {coins}')
if count_0 < count_1:
	print(f'Минимальное количество монеток, которые нужно перевернуть: {count_0}')
else:
	print(f'Минимальное количество монеток, которые нужно перевернуть: {count_1}')
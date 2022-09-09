# Напишите программу, которая найдёт произведение пар чисел списка. Парой 
# считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from os import system

system('cls')

arr = [2, 3, 4, 5, 6]
if len(arr) < 2:
	print('ОШИБКА! В списке нет пар!')
	exit()
result = []
for i in range(len(arr) // 2):
	result.append(arr[i] * arr[len(arr) - i - 1])

if len(arr) % 2 != 0:
	result.append(arr[len(arr) // 2] ** 2)

print(f'{arr} => {result}')

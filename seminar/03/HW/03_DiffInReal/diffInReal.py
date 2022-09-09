# Задайте список из вещественных чисел. Напишите программу, которая найдёт
# разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from os import system

system('cls')

arr = [1.1, 1.2, 3.1, 5, 10.01]
max = arr[0] % 1
min = arr[0] % 1
for i in range(1, len(arr)):
	if arr[i] % 1 > max and arr[i] % 1 != 0:
		max = arr[i] % 1
	if arr[i] % 1 < min and arr[i] % 1 != 0:
		min = arr[i] % 1

print(f'{arr} => {round(max - min, 3)}')

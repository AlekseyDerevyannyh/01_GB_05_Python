# Задайте последовательность чисел. Напишите программу, которая выведет
# список неповторяющихся элементов исходной последовательности.

from os import system

system('cls')

list1 = [2, 7, 7, -3, -8, -3, -3, -3, 0, 3, 2, 7, 2, 2, 2, 2, 7]

i = 0
while i < len(list1):
	j = i + 1
	while j < len(list1):
		if list1[i] == list1[j]:
			list1.pop(j)
			j = i + 1
		else:
			j += 1
	i += 1

print(list1)

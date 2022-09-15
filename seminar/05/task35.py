# 35. В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i - 1]. 
# Найдите это число.

from os import system

system('cls')

def search_number(arr):
	for i in range(1, len(arr)):
		if arr[i] - 1 != arr[i - 1]:
			return i + 1
	return 'Последовательность верна'


with open('numbers.txt', 'r', encoding='utf-8') as file:
	arr = [int(i) for i in file.read().split()]
print(search_number(arr))

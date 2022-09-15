# Два различных натуральных числа называются дружественными, если первое из них равно
# сумме делителей второго числа, за исключением самого второго числа, а второе равно
# сумме делителей первого числа, за исключением самого первого числа. Требуется найти все
# пары дружественных чисел, оба из которых принадлежат промежутку от M до N.
# Входные данные
# В первой строке находятся целые числа M и N (1  ≤ M ≤ N ≤ 1 000 000).
# Выходные данные
# В каждой строке вывести по паре чисел через пробел. Первое число пары должно быть меньше
# второго. Строки должны быть отсортированы в порядке возрастания первого числа пары. Если
# пар дружественных чисел в промежутке нет, вывести "Absent".

from os import system

def SumOfDivisors (number):
	result = 0
	for i in range(1, number):
		if number % i == 0:
			result += i
	return result

def CheckElementInList(list1, value):
	result = False
	for i in range(len(list1)):
		for j in range(len(list1[i])):
			if list1[i][j] == value:
				result = True
	return result

system('cls')

m = int(input('Введите число M: '))
n = int(input('Введите число N: '))
if m >= n or m < 1 or n < 1 or m > 1000000 or n > 1000000:
	print('Ошибка ввода!')
	exit()
print(m, n)

flagFriendly = False
listFriendly = []
for i in range(m, n + 1):
	sumOfDivisors_i = SumOfDivisors(i)
	if sumOfDivisors_i <= n and sumOfDivisors_i > m and SumOfDivisors(sumOfDivisors_i) == i:
		if i < sumOfDivisors_i:
			if not CheckElementInList(listFriendly, i):
				listFriendly.append([i, sumOfDivisors_i])
		elif i > sumOfDivisors_i:
			if not CheckElementInList(listFriendly, sumOfDivisors_i):
				listFriendly.append([sumOfDivisors_i, i])
		flagFriendly = True
if flagFriendly:
	for i in range(len(listFriendly)):
		print(*listFriendly[i])
else:
	print('Absent')

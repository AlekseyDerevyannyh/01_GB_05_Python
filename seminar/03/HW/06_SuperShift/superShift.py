# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть
# всю последовательность (сдвиг - циклический) на |K| элементов вправо,
# если K – положительное и влево, если отрицательное.

from os import system

system('cls')

arr = [1, 2, 3, 4, 5, 6, 7]
print(arr)
k = int(input('Введите число k для сдвига: '))
if k == 0:
	print(arr)
	exit()

shift = k
if abs(k) >= len(arr):		# оптимизация количества сдвигов, если их больше количества элементов списка
	if k > 0:
		shift %= len(arr)
	else:
		shift %= -len(arr)

if shift > 0:
	for i in range(shift):
		tmp1 = arr[-1]
		tmp2 = 0
		for j in range(len(arr)):
			tmp2 = arr[j]
			arr[j] = tmp1
			tmp1 = tmp2
else:
	for i in range(abs(shift)):
		tmp1 = arr[0]
		tmp2 = 0
		for j in range(len(arr) - 1, -1, -1):
			tmp2 = arr[j]
			arr[j] = tmp1
			tmp1 = tmp2

print(arr)

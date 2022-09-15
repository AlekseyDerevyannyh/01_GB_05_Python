# 36. Дан список чисел. Создайте список, в который попадают числа, 
# описываемые возрастающую последовательность. 
# Порядок элементов менять нельзя.
#     *Пример:* 
#     [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

from os import system
from random import randint as rd

system('cls')

arr = [1, 5, 2, 3, 4, 6, 1, 7]
index_randomNumber = rd(0, len(arr) - 1)
randomNumber = arr[index_randomNumber]
result_list = [randomNumber]
for i in range(index_randomNumber + 1, len(arr)):
	if arr[i] > randomNumber:
		result_list.append(arr[i])
		randomNumber = arr[i]
print(result_list)

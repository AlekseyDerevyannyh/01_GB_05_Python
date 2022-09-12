# Задайте строку из набора чисел. Напишите программу, которая покажет большее и 
# меньшее число. В качестве символа-разделителя используйте пробел.

from os import system

system('cls')

stroka = '3, 4, 5, 6'
x = stroka.split(', ')
for i in range(len(x)):
	x[i] = int(x[i])
max_list = x[0]
min_list = x[0]
for i in x:
	if max_list < i:
		max_list = i
	if min_list > i:
		min_list = i
print(max_list, min_list)

# Программа рисования таблицы бинарных операций

from os import system

system('cls')

def print_operation_table(operation, num_rows = 9, num_columns = 9):
	if num_rows < 2 or num_columns < 2:
		print('ОШИБКА! Размерности таблицы должны быть больше 2!')
		exit()
	print('	'.join([str(i) for i in range(1, num_columns + 1)]))
	for i in range(2, num_rows + 1):
		print(i, end = '	')
		for j in range(2, num_columns + 1):
			print(operation(i, j), end = '	')
		print()

print_operation_table(lambda x, y: x * y)

import csv

def write_table (path):
	with open(path, 'r', encoding = 'utf-8') as file:
		header = list(csv.reader(file, delimiter = ';'))[0][1:]
	with open(path, 'r', encoding = 'utf-8') as file:
		data = list(csv.reader(file, delimiter = ';'))[-1]
	last_id = int(data[0])
	result = [str(last_id + 1)]
	for i in header:
		result.append(input(f'Введите {i}: '))

	with open (path, 'a+', encoding = 'utf-8') as file:
		for i in result[:-1]:
			file.write(f'{i};')
		file.write(f'{result[-1]}\n')
	print('Информация добавлена')

def remove_from_table (path):
	id_input = input('Введите id строки для удаления: ')
	with open(path, 'r', encoding = 'utf-8') as file:
		data = list(csv.reader(file, delimiter = ';'))
	result = [data[0]]
	correct_input = False
	for i in data[1:]:
		if id_input != i[0]:
			result.append(i)
		else:
			correct_input = True
	
	if correct_input:
		with open (path, 'w', encoding = 'utf-8') as file:
			for i in result:
				for j in i[:-1]:
					file.write(f'{j};')
				file.write(f'{i[-1]}\n')
		print(f'Строка {id_input} удалена из таблицы')
	else:
		print(f'Строки с id = {id_input} не существует')

def change_in_table (path):
	id_input = input('Введите id строки для внесения изменений: ')
	with open(path, 'r', encoding = 'utf-8') as file:
		data = list(csv.reader(file, delimiter = ';'))
	result = [data[0]]
	correct_input = False
	for i in data[1:]:
		if id_input == i[0]:
			changed_string = [i[0]]
			for j in data[0][1:]:
				changed_string.append(input(f'Введите {j}: '))
			result.append(changed_string)
			correct_input = True
		else:
			result.append(i)

	if correct_input:
		with open (path, 'w', encoding = 'utf-8') as file:
			for i in result:
				for j in i[:-1]:
					file.write(f'{j};')
				file.write(f'{i[-1]}\n')
		print(f'В строку {id_input} внесены изменения')
	else:
		print(f'Строки с id = {id_input} не существует')

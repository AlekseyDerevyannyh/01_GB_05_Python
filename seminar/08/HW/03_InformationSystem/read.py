import csv

def read_table (path):
	with open(path, 'r', encoding = 'utf-8') as file:
		data = list(csv.reader(file, delimiter = ';'))
		for i in data:
			print('\t'.join(i))

def search_in_table (path, value = '', table_name = ''):
	with open(path, 'r', encoding = 'utf-8') as file:
		header = list(csv.reader(file, delimiter = ';'))[0]
	with open(path, 'r', encoding = 'utf-8') as file:
		data = list(csv.reader(file, delimiter = ';'))[1:]
	result = [i for i in data for j in i if value.lower() in j.lower()]
	if result:
		print(f'Совпадения в таблице "{table_name}":')
		print('\t'.join(header))
		for i in result:
			print('\t'.join(i))
	else:
		print(f'В таблице "{table_name}" ничего не найдено!')

def search_in_tables (tables, value):
	for i in range(len(tables)):
		search_in_table(tables[i][1], value, tables[i][0])
		print()

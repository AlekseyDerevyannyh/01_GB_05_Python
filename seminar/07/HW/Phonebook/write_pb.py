def write_phonebook (path):
	name = input('Введите ФИО: ')
	phone = input('Введите телефон: ')
	with open(path, 'a+', encoding = 'UTF-8') as file:
		file.write(f'ФИО: {name}. Тел.: {phone}\n')
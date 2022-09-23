def write_phonebook ():
	name = input('Введите ФИО: ')
	phone = input('Введите телефон: ')
	with open('seminar/07/HW/Phonebook/phonebook.txt', 'a+', encoding = 'UTF-8') as file:
		file.write(f'ФИО: {name}. Тел.: {phone}\n')
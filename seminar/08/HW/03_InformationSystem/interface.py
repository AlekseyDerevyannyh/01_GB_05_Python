from read import *
from write import *
from os import system

path_timetable = 'timetable.csv'
path_teachers = 'teachers.csv'
path_contacts = 'contacts.csv'

def menu ():
	
	while True:
		system('cls')

		print('Информационна система школы\n')
		print('1. Вывести список таблиц')
		print('2. Вывести таблицу')
		print('3. Поиск')
		print('4. Добавить новые данные в таблицу')
		print('5. Удалить данные из таблицы')
		print('6. Изменить данные в таблице')
		print('7. Выход из программы\n')
		
		tables = [('Расписание', path_timetable), ('Учителя', path_teachers), ('Контакты учеников', path_contacts)]
		answer = 0
		while answer < 1 or answer > 7:
			answer = int(input('Введите действие: '))
		if answer == 1:
			for i in range(len(tables)):
				print(f'{i + 1}. {tables[i][0]}')
			input('Нажмите "Enter" для продолжения > ')
		elif answer == 2:
			system('cls')
			answer2 = select_table(tables)
			read_table(tables[answer2 - 1][1])
			input('Нажмите "Enter" для продолжения > ')
		elif answer == 3:
			search_in_tables(tables, input('Введите данные для поиска: '))
			input('Нажмите "Enter" для продолжения > ')
		elif answer == 4:
			system('cls')
			answer2 = select_table(tables)
			read_table(tables[answer2 - 1][1])
			write_table(tables[answer2 - 1][1])
			input('Нажмите "Enter" для продолжения > ')
		elif answer == 5:
			system('cls')
			answer2 = select_table(tables)
			read_table(tables[answer2 - 1][1])
			remove_from_table(tables[answer2 - 1][1])
			input('Нажмите "Enter" для продолжения > ')
		elif answer == 6:
			system('cls')
			answer2 = select_table(tables)
			read_table(tables[answer2 - 1][1])
			change_in_table(tables[answer2 - 1][1])
			input('Нажмите "Enter" для продолжения > ')
		elif answer == 7:
			exit()

def select_table (tables):
	for i in range(len(tables)):
		print(f'{i + 1}. {tables[i][0]}')
	answer = 0
	while answer < 1 or answer > 3:
		answer = int(input('Введите номер таблицы: '))
	return answer

from read_pb import read_phonebook
from write_pb import write_phonebook
from search import search_contact
from import_csv import import_to_csv
from os import system

path_phonebook_txt = 'phonebook.txt'
path_pnonebook_csv = 'phonebook.csv'

def menu ():
	
	while True:
		system('cls')

		print('Телефонный справочник\n')
		print('1. Вывести телефонный справочник')
		print('2. Поиск контакта')
		print('3. Добавить новый контакт в справочник')
		print('4. Импорт справочника в .csv')
		print('5. Выход из программы\n')
		
		answer = 0
		while answer < 1 or answer > 5:
			answer = int(input('Введите действие: '))
		if answer == 1:
			read_phonebook(path_phonebook_txt)
			input('Нажмите "Enter" для продолжения > ')
		elif answer == 2:
			search_contact(path_phonebook_txt, input('Введите данные контакта: '))
			input('Нажмите "Enter" для продолжения > ')
		elif answer == 3:
			write_phonebook(path_phonebook_txt)
		elif answer == 4:
			import_to_csv(path_phonebook_txt, path_pnonebook_csv)
		elif answer == 5:
			exit()

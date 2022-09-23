from read_pb import read_phonebook
from write_pb import write_phonebook
from search import search_contact
from os import system

def menu ():
	
	while True:
		system('cls')

		print('Телефонный справочник\n')
		print('1. Вывести телефонный справочник')
		print('2. Поиск контакта')
		print('3. Добавить новый контакт в справочник')
		print('4. Выход из программы\n')
		
		answer = ''
		while answer != '1' and answer != '2' and answer != '3' and answer != '4':
			answer = input('Введите действие: ')
		if answer == '1':
			read_phonebook()
			input('Нажмите "Enter" для продолжения > ')
		elif answer == '2':
			search_contact(input('Введите данные контакта: '))
			input('Нажмите "Enter" для продолжения > ')
		elif answer == '3':
			write_phonebook()
		elif answer == '4':
			exit()

menu()

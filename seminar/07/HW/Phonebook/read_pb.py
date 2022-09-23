def read_phonebook ():
	data = open('seminar/07/HW/Phonebook/phonebook.txt', 'r', encoding = 'UTF-8')

	phones = [line[:-1] for line in data]
	phones.sort()
	for contact in phones:
		print(contact)
	data.close()
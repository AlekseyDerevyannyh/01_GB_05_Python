def read_phonebook ():
	data = open('seminar/07/HW/Phonebook/phonebook.txt', 'r', encoding = 'UTF-8')

	phones = []
	for line in data:
		phones.append(line[:-1])
	phones.sort()
	for contact in phones:
		print(contact)
	data.close()
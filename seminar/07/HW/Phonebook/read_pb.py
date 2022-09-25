def read_phonebook (path):
	data = open(path, 'r', encoding = 'UTF-8')

	phones = [line[:-1] for line in data]
	phones.sort()
	for contact in phones:
		print(contact)
	data.close()
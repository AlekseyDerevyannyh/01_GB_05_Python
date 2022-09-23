def search_contact (value):
	data = open('seminar/07/HW/Phonebook/phonebook.txt', 'r', encoding = 'UTF-8')

	phones = []
	for line in data:
		phones.append(line[:-1])
	result = []
	for contact in phones:
		if value.lower() in contact.lower():
			result.append(contact)
	for contact in result:
		print(contact)
	data.close()
def search_contact (value):
	data = open('seminar/07/HW/Phonebook/phonebook.txt', 'r', encoding = 'UTF-8')

	phones = [line[:-1] for line in data]
	result = [contact for contact in phones if value.lower() in contact.lower()]

	for contact in result:
		print(contact)
	data.close()
def search_contact (path, value):
	data = open(path, 'r', encoding = 'UTF-8')

	phones = [line[:-1] for line in data]
	result = [contact for contact in phones if value.lower() in contact.lower()]

	for contact in result:
		print(contact)
	data.close()
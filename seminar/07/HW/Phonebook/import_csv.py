def import_to_csv (path_txt, path_csv):
	data = open(path_txt, 'r', encoding = 'UTF-8')
	phones = [line[:-1] for line in data]
	data.close()

	phones.sort()
	with open(path_csv, 'w') as file:
		file.write('ФИО;Тел.\n')
		for contact in phones:
			result = contact.split('. Тел.: ')
			file.write(f'{result[0][5:]};{result[1]}\n')

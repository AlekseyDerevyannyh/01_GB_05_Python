import csv

with open('data.csv', 'r', encoding='utf-8') as file:
	data = csv.reader(file, delimiter=';')
for i in data:
	print(i)

# Пам-парам парам-пам парам

from os import system

system('cls')

stroka1 = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
vowels = ['а', 'е', 'ё', 'и', 'й', 'о', 'у', 'ы', 'э', 'ю', 'я']
phrases = stroka1.split()
if len(phrases) < 2:
	print('Количество фраз должно быть больше одной!')
	exit()

countVowels = []

for i in phrases:
	countVowels.append(len([x for x in i if x in vowels]))

if countVowels.count(countVowels[0]) == len(countVowels):
	print('Парам пам-пам')
else:
	print('Пам парам')

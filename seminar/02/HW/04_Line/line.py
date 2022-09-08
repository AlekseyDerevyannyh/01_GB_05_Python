# Петя впервые пришел на урок физкультуры в новой школе. Перед началом урока
# ученики выстраиваются по росту, в порядке невозрастания. Напишите программу,
# которая определит на какое место в шеренге Пете нужно встать, чтобы не нарушить
# традицию, если заранее известен рост каждого ученика и эти данные уже расположены
# по невозрастанию (то есть каждое следующее число не больше предыдущего).
# Если в классе есть несколько учеников с таким же ростом, как у Пети, то программа
# должна расположить его после них.

from os import system
from random import randint

system('cls')

n = int(input('Введите количество учеников: '))
studentsHeight = list(range(n))
for i in studentsHeight:
	studentsHeight[i] = randint(100, 200)		# формируем список ростов учеников

studentsHeight.sort(reverse = True)				
print(f'Шеренга учеников по росту: {studentsHeight}')

heightPetya = int(input('Введите рост Пети: '))
numberPetya = 1
for i in studentsHeight:
	if heightPetya <= i:
		numberPetya += 1
print(f'Номер Пети в шеренге: {numberPetya}')
# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход
# друг после друга. Первый ход определяется жеребьёвкой. За один ход можно
# забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему
# последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота

from os import system
from random import randint

system('cls')

candiesOnTable = 2021
candiesLimit = 28
candiesGamers = [0, 0]
gamer = randint(0, 1)		# Жеребьёвка. 0 - ходит игрок. 1 - ходит бот
if gamer:	print('Результат жеребьёвки: первым ходит бот')
else:		print('Результат жеребьёвки: первым ходит игрок')
winner = 0

while candiesOnTable:
	print()
	print('игрок	стол	бот')
	print(f'{candiesGamers[0]}	{candiesOnTable}	{candiesGamers[1]}')
	if gamer:
		candies = candiesOnTable % (candiesLimit + 1)
		print(f'Бот забирает конфет: {candies}')
	else:
		candies = int(input('Сколько конфет забирает игрок?: '))

	# Защита от нарушений правил игры
	if candies > candiesLimit:	candies = candiesLimit
	elif candies < 1:			candies = 1

	if candies >= candiesOnTable:
		candiesOnTable = 0
		winner = gamer
	else:
		candiesGamers[gamer] += candies
		candiesOnTable -= candies
		gamer = int(not gamer)

if winner:	print('Победил бот')
else:		print('Победил игрок')
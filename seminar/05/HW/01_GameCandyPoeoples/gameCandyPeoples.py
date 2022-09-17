# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход
# друг после друга. Первый ход определяется жеребьёвкой. За один ход можно
# забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему
# последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?

from os import system
from random import randint

system('cls')

candiesOnTable = 500
candiesLimit = 28
candiesPlayer1 = 0
candiesPlayer2 = 0
player = randint(0, 1)		# Жеребьёвка. 0 - ходит первый игрок. 1 - ходит второй игрок

winner = 0

while candiesOnTable:
	# system('cls')
	print('')
	print('1-ый игрок	стол	2-ой игрок')
	print(f'{candiesPlayer1}		{candiesOnTable}	{candiesPlayer2}')
	if not player:
		candies = int(input('Сколько конфет забирает 1-ый игрок?: '))
		if candies > candiesLimit:
			candies = candiesLimit
		if candies >= candiesOnTable:
			candiesOnTable = 0
			winner = 0
		else:
			candiesPlayer1 += candies
			candiesOnTable -= candies
			player = 1
	else:
		candies = int(input('Сколько конфет забирает 2-ой игрок?: '))
		if candies > candiesLimit:
			candies = candiesLimit
		if candies >= candiesOnTable:
			candiesOnTable = 0
			winner = 1
		else:
			candiesPlayer2 += candies
			candiesOnTable -= candies
			player = 0

print(f'Победил игрок {winner + 1}')

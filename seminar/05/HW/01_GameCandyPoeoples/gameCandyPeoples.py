# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход
# друг после друга. Первый ход определяется жеребьёвкой. За один ход можно
# забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему
# последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?

from os import system
from random import randint

system('cls')

candiesOnTable = 2021
candiesLimit = 28
candiesGamers = [0, 0]
gamer = randint(0, 1)		# Жеребьёвка. 0 - ходит первый игрок. 1 - ходит второй игрок
print(f'Результат жеребьёвки: первым ходит игрок {gamer + 1}')
winner = 0

while candiesOnTable:
	print('')
	print('1-ый игрок	стол	2-ой игрок')
	print(f'{candiesGamers[0]}		{candiesOnTable}	{candiesGamers[1]}')
	candies = int(input(f'Сколько конфет забирает игрок {gamer + 1}?: '))
	if candies > candiesLimit:
		candies = candiesLimit
	if candies >= candiesOnTable:
		candiesOnTable = 0
		winner = gamer
	else:
		candiesGamers[gamer] += candies
		candiesOnTable -= candies
		if gamer:	gamer = 0
		else:		gamer = 1

print(f'Победил игрок {winner + 1}')

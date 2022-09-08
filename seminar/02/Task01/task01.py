# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
# *Пример:*
# - Для N = 5: 1, -3, 9, -27, 81

from os import system
system('cls')

# n = int(input('Введите число N: '))
# step = 1
# for i in range(n):
# 	print(step, end = ' ')
# 	step *= -3

print(*[(-3) ** i for i in range(int(input('Введите число N: ')))])
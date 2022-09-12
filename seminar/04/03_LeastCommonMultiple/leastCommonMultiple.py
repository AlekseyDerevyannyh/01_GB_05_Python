# Задайте два числа. Напишите программу, которая 
# найдёт НОК (наименьшее общее кратное) этих двух чисел.

from os import system

system('cls')

a = int(input())
b = int(input())
p = a * b

while a != 0 and b != 0:
	if a > b:
		a = a % b
	else:
		b = b % a
nod = a + b
nok = p // nod
print(nok)

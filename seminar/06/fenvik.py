from os import system
from math import log2

system('cls')

n = int(input())
i = round(log2(n)) + 1
if n % 2 != 0:
	print(1)
else:
	flag = True
	while flag:
		if n % 2 ** i == 0:
			print(2 ** i)
			flag = False
		i -= 1
	if flag:
		print(1)

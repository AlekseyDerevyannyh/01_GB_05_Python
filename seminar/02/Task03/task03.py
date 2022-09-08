# 3. Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.

from os import system
system('cls')

stroka1 = input()
stroka2 = input()
print(stroka1.count(stroka2))

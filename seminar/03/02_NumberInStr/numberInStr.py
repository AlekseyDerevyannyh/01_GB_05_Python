# 2. Задайте список. Напишите программу, которая определит, 
# присутствует ли в заданном списке строк некое число.

from os import system

system('cls')

arr = ['bbb21dd', 'Hello', 'World']
n = '21'
flag = False
for stroka in arr:
    if n in stroka:
        flag = True
        print('yes')
if flag == False:
    print('no')

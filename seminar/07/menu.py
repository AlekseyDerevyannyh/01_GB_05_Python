from function import plus, minus, div, umnoj
from log import print_result

def start():
	var = input('Добро пожаловать! Это калькулятор! Выбери с какими числами, Вы хотите работать\n1-рациональные\n2-комплексные\n')

	if var == '1':
		number_first = float(input("Введите первое число: "))
		number_second = float(input("Введите второе число: "))
	if var == '2':
		number_first = complex(input("Введите первое число: "))
		number_second = complex(input("Введите второе число: "))
	answer = input("Какую мат. операцию Вы хотите применить?(+,-,*,/): ")
	if answer == '+':
		result = plus(number_first, number_second)
	elif answer == '-':
		result = minus(number_first, number_second)
	elif answer == '*':
		result = umnoj(number_first, number_second)
	elif answer == '/':
		result = div(number_first, number_second)
	print_result(result, number_first, number_second, answer)

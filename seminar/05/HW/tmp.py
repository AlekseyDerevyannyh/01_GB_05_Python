def IsNumber (symbol):
	numberList = [str(i) for i in range(10)]
	for i in numberList:
		if symbol == i:
			return True
	return False

print(IsNumber('1'))
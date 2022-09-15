# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

from os import system

system('cls')

def StrPolynomToCoefList (polynom):
	list1 = polynom.split(' + ')
	list1[-1] = list1[-1][0:-4]

	for i in range(len(list1)):
		list1[i] = list1[i].replace('*x^', ' ')
		list1[i] = list1[i].replace('x^', '1 ')
		list1[i] = list1[i].replace('*x', ' 1')
		list1[i] = list1[i].replace('x', '1 1')

	list2 = []
	for i in range(len(list1)):
		list2.append(list1[i].split(' '))

	for i in range(len(list2)):
		if len(list2[i]) < 2:
			list2[i].append('0')

	for i in range(len(list2)):
		for j in range(2):
			list2[i][j] = int(list2[i][j])

	max = list2[0][1]
	for i in range(1, len(list2)):
		if list2[i][1] > max:
			max = list2[i][0]

	coefList = []
	for i in range(max + 1):
		coefList.append(0)

	for i in range(len(coefList)):
		for j in range(len(list2)):
			if list2[j][1] == i:
				coefList[len(coefList) - i - 1] = list2[j][0]
	return coefList

def CoefListToStrPolynom (coefList):
	polynom = ''
	for i in range(len(coefList) - 1):
		if coefList[i] == 0:
			if coefList[i + 1] != 0:
				polynom = polynom + ' + '
		elif coefList[i] == 1:
			if coefList[i + 1] != 0:
				if len(coefList) - i - 1 == 1:
					polynom = polynom + f'x + '
				else:
					polynom = polynom + f'x^{len(coefList) - i - 1} + '
			else:
				if len(coefList) - i - 1 == 1:
					polynom = polynom + f'x'
				else:
					polynom = polynom + f'x^{len(coefList) - i - 1}'
		else:
			if coefList[i + 1] != 0:
				if len(coefList) - i - 1 == 1:
					polynom = polynom + f'{coefList[i]}*x + '
				else:
					polynom = polynom + f'{coefList[i]}*x^{len(coefList) - i - 1} + '
			else:
				if len(coefList) - i - 1 == 1:
					polynom = polynom + f'{coefList[i]}*x'
				else:
					polynom = polynom + f'{coefList[i]}*x^{len(coefList) - i - 1}'

	if coefList[-1] != 0:
		polynom = polynom + f'{coefList[-1]} = 0'
	else:
		polynom = polynom + ' = 0'
	return polynom

data = open('polynom1.txt', 'r')
polynom1 = data.read()
data.close()

data = open('polynom2.txt', 'r')
polynom2 = data.read()
data.close()

coefList1 = StrPolynomToCoefList(polynom1)
coefList2 = StrPolynomToCoefList(polynom2)
if len(coefList1) < len(coefList2):
	for i in range(len(coefList2 - coefList1)):
		coefList1.insert(0, 0)
elif len(coefList1) > len(coefList2):
	for i in range(len(coefList1) - len(coefList2)):
		coefList2.insert(0, 0)

coefListSum = []

for i in range(len(coefList1)):
	coefListSum.append(coefList1[i] + coefList2[i])

data = open('polynomSum.txt', 'w')
data.write(CoefListToStrPolynom(coefListSum))
data.close

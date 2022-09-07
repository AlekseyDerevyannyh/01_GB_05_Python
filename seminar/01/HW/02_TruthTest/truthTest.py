# Напишите программу для. проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

from os import system
system('cls')

x = [False, True]
y = [False, True]
z = [False, True]

result = True
for i in x:
	for j in y:
		for k in z:
			if not (not (x[i] and y[j] and z[k]) == (not x[i] or not y[j] or not z[k])):
				result = False

if result:
	print('Утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z - истинно')
else:
	print('Утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z - ложно')

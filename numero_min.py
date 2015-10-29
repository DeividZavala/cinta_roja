"""NUmero menor"""

numero_min = map(int,raw_input('Escribe una serie de numeros ').split())

minimo = numero_min[0]

for number in numero_min:
	if (number) < minimo:
		minimo = number

print 'El numero minimo es ', minimo
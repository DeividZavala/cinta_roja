"""Suma Rango"""

a,b = map(int,raw_input('dame dos valores, uno de inicio y otro de fin ').split())

# a = input('Introduce un valor de inicio ')
# b = input('Introduce un valor de fin ')

if a < b:
	suma = a

	for i in range(a+1,b+1):
		suma = suma + i
	print suma

elif a > b:
	
	suma = b

	for i in range(b+1,a+1):
		suma = suma + (i)
	print suma
else:
	print 'No es un rango valido'

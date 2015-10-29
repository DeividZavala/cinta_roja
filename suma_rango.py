"""Suma Rango"""

#  a,b = map(int,raw_input('dame dos valores ').split())

a = input('Introduce un valor de inicio ')
b = input('Introduce un valor de fin ')

suma = a

for i in range(a+1,b+1):
	suma = suma + i
print suma
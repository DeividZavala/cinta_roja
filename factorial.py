"""factorial"""

n = int(input('Ingresa un numero '))

producto = 1
if n > 0:
	for x in range(1,n+1):
		producto = producto * x
	print producto
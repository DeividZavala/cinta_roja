"""potencia"""

a,b = map(int,raw_input('Escribe la base y el exponente ').split())

def potencia(a, b):
	if b <= 0:
		return 1
	return a * potencia(a,b-1)
print potencia(a,b)


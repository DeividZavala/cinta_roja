"""Maximo comun divisor"""

# def mcd(a, b):
# 	holi = min(a, b)

# 	while a % holi != 0 or b % holi != 0:
# 		holi -= 1
# 	return holi

#   Recursiva

a,b = map(int,raw_input('Escribe los valores ').split())

def mcd(a, b):
	if b == 0:
		return a
	return mcd(b, a % b)
print mcd(b,a%b)
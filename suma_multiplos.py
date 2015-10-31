"""suma de multiplos"""

multi3 = []
multi5 = []

for i in range(1000):
	if i % 3 == 0:
		multi3.append(i)
	elif i % 5 == 0:
		multi5.append(i)

suma1  = sum(multi3)
suma2 = sum(multi5)
suma3 = suma1 + suma2
print suma3



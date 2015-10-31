"""suma de multiplos"""

multiplos = []

for i in range(1000):
	if i % 3 == 0 or i % 5 == 0:
		multiplos.append(i)

suma1  = sum(multiplos)

print suma1



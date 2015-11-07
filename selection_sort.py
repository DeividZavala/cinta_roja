"""Selection sort"""

from random import sample

n=input("Ingresa tu numero: ")
l=sample(range(1,n+1),n)
print l
for i in range(0,len(l)):
	minimo= l[i]
	for j in range(i,len(l)):
		if l[j]<l[i]:
			minimo = l[j]
			l[j],l[i]=l[i],l[j]
			
print l
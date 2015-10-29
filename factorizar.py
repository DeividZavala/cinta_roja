"""Chicharronera"""

import math

a = input('valor de a ')
b = input('valor de b ')
c = input('valor de c ')

if (math.sqrt(math.pow(b, 2)-(4*a*c))) >= 0:
	formula1 = (-b + (math.sqrt(math.pow(b, 2)-(4*a*c))))/(2*a)
	formula2 = (-b - (math.sqrt(math.pow(b, 2)-(4*a*c))))/(2*a)
else:
	print "no pasa"

print 'X1 = ', formula1
print 'X2 = ', formula2
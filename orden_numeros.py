"""Ordenar numeros"""

# a  = input('a: ')
# b  = input('b: ')
# c  = input('c: ')

# if a < b and a < c:
# 	print a
# 	if b < c:
# 		print b 
# 		print c
# 	else:
# 		print c
# 		print b

# elif b < a and b < c:
# 	print b
# 	if a < c:
# 		print a
# 		print c
# 	else:
# 		print c
# 		print a
# else:
# 	print c
# 	if a < b:
# 		print a
# 		print b
# 	else:
# 		print b
# 		print a

#     manera corta

numbers = map(int,raw_input('Escribe los numeros ').split())
numbers2 = []

def get_min(my_list):
	minimun = my_list[0]
	for number in my_list:
		if number < minimun:
			minimun = number
	return minimun

while len(numbers) > 0:
	minimun = get_min(numbers)
	numbers.remove(minimun)
	numbers2.append(minimun)
print numbers2
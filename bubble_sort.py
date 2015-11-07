"""Ordenamiento bubble"""

from random import sample

def bubble_sort (u):
	keep_sorting = True
	interation_length = len(u) - 1
	while keep_sorting:
		keep_sorting = False
		for i in range(interation_length):
			if u[i] > u[i+1]:
				keep_sorting = True
				u[i], u[i+1] = u[i+1], u[i]
		interation_length -= 1
	return u

n = map(int,raw_input('random number to sort: ').split())
random_numbers = sample(n,len(n))
print 'Unsorted', random_numbers
bubble_sort(random_numbers)
print 'Sorted:',random_numbers
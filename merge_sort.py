""" Merge sort by everyone """

def get_merge(lst1, lst2):
	merge_list = []

	while  len(lst1) > 0 and len(lst2) > 0:
		if lst1[0] < lst2[0]:
			merge_list.append(lst1.pop(0))
		else:
			merge_list.append(lst2.pop(0))

	if len(lst1) > 0:
		for i in range(len(lst1)):
			merge_list.append(lst1.pop(0))
	else:
		for i in range(len(lst2)):
			merge_list.append(lst2.pop(0))
			
	return merge_list


def merge_sort(lst):
	print lst
	if len(lst) == 0:
		return []
	if len(lst) == 1:
		return lst

	half = ((len(lst)-1)/2 + 1)

	left = lst[:half]
	right = lst[half:]

	return get_merge(merge_sort(left), merge_sort(right))

lst = map(int,raw_input('Escribe los numeros aqui: ').split())

print merge_sort(lst)
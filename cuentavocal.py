"""Counting"""

text = raw_input('give me a string')

vowels = 'aeiouAEIOU'
count = 0
for letter in text:
	if letter in vowels:
		count += 1
print 'there are ',count, 'vowels in ',text
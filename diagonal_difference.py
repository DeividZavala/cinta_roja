"""diagonal diference"""

n = int(raw_input())
number = []
for i in range(n):
	number.append(map(int,raw_input().split()))

sum1 = 0
sum2 = 0
for i in range(n):
	sum1 += number[i][i]

j = n -1
for i in range(n):
	sum2 += number[j][i]
	j -= 1

print abs(sum1 - sum2)
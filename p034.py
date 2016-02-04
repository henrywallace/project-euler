from operator import mul
from functools import reduce

def fact(n):
	assert(n >= 0)
	if n <= 1:
		return 1
	return reduce(mul, range(1, n + 1))

# calculate bound on number of digits
k = 1
while 10**k < k*fact(9):
	k += 1
print(k)

nums = []
for n in range(10, 10**k):
	if sum(fact(int(x)) for x in str(n)) == n:
		nums.append(n)
print(nums)
print(sum(nums))
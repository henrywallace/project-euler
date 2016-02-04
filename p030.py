p = 5

# first bound on number of digits k before power sum is impossible 
k = 1
while 10**k < k*(9**p):
	k += 1
print(k)

nums = []
for n in range(10, 10**k):	# start with first number that has "sum"
	if n == sum(int(x)**p for x in str(n)):
		nums.append(n)
print(nums)
print(sum(nums))
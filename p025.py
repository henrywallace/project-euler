prev = 0
curr = 1
i = 1
while len(str(curr)) < 1000:
	prev, curr = curr, prev + curr
	i += 1
print(i)
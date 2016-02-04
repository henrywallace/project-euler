s = 0
prev, curr = 0, 1
while curr < 4*10**6:
	if curr % 2 == 0:
		s += curr
	prev, curr = curr, prev + curr

print(s)
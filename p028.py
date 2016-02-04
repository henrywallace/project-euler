def spirals(side_len):
	steps = side_len//2
	n, k = 1, 2
	yield n
	for _ in range(steps):
		for _ in range(4):
			n += k
			yield n
		k += 2

print(sum(spirals(1001)))
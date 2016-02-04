bound = 500
for c in range(2, bound + 1):
	for b in range(2, bound + 1):
		for a in range(2, bound + 1):
			if a**2 + b**2 == c**2 and a + b + c == 1000:
				print(a*b*c)
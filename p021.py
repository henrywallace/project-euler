def div_sum(n):
	if n == 1:
		return 0
	s = 0
	for d in range(1, int(n**0.5) + 1):
		if n % d == 0:
			s += d
			if d != 1 and n//d != d:
				s += n//d
	return s

amicable = set()
for n in range(1, 10**4):
	b = div_sum(n)
	if b in amicable or b == n:
		continue
	elif div_sum(b) == n:
		amicable.add(n)
		amicable.add(b)
print(sorted(amicable))
print(sum(amicable))

from math import log

def pandigital(num_str):
	if len(num_str) != 9:
		return False
	seen = set()
	for c in num_str:
		if c in seen or c == '0':
			return False
		seen.add(c)
	return True

s = 0
seen = set()
for a in range(1, 10**4):  # since 3*4 > 10, but 3*3 < 10
	t = int(log(a, 10)) + 1
	b = 1
	p = a*b
	while p < 10**((10 - t)//2 + 1):
		if pandigital(str(a) + str(b) + str(p)):
			print(a, b, p)
			if p not in seen:
				s += p
				seen.add(p)
		b += 1
		p = a*b
print(s)
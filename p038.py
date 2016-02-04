"""Notice that a 5 digit integer, m, multiplied by 2 is again 5 digits. So using the minimum n, their concatenation exceeds the number of digits in the sought pandigital."""

def pandigital(num_str):
	if len(num_str) != 9:
		return False
	seen = set()
	for c in num_str:
		if c in seen or c == '0':
			return False
		else:
			seen.add(c)
	return True

max_pan, max_mn = 0, (0, 0)
for m in range(1, 10**5):
	s = ''
	n = 1
	while len(s) < 9:
		s += str(n*m)
		n += 1
	if pandigital(s) and int(s) > max_pan:
		max_pan, max_mn = int(s), (m, n - 1)
print(max_pan, max_mn)
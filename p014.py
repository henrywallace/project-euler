def collatz(n):
	if n % 2 == 0:
		return n // 2
	elif n == 1:
		return 1
	else:
		return 3*n + 1

def chain_len(n, d):
	x = collatz(n)
	k = 1
	while x != 1:
		if x in d:
			return k + d[x]
		else:
			x = collatz(x)
			k += 1
	else:
		return k + 1

def longest_chain(bound):
	d = {}
	m, l = 1, 1
	for n in range(1, bound):
		d[n] = chain_len(n, d)
		if d[n] > l:
			m, l, = n, d[n]
	return m, l

print(longest_chain(10**6))
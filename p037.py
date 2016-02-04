def primes():
	# continuously generates new primes
	yield 2
	ps = [2]
	k = 3
	while True:
		s = int(k**0.5) + 1
		for p in ps:
			if k % p == 0:
				break
			if p > s:
				ps.append(k)
				yield k
				break
		else:
			ps.append(k)
			yield k
		k += 2

def truncatable(p, pool):
	# assumes p is prime
	if p < 11:
		return False
	s = str(p)
	return all(int(s[i:]) in pool for i in range(len(s))) \
		and all(int(s[:-(i + 1)]) in pool for i in range(len(s) - 1))

pool = set()
truncs = []
for p in primes():
	if len(truncs) == 11:
		break
	pool.add(p)
	if truncatable(p, pool):
		truncs.append(p)
		print(p)
print('>', sum(truncs))
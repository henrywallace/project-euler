"""Rather then continuously checking if integers are primes, we shall generate them quickly using a sieve."""

from itertools import chain, product

def prime_list(n):
	# generate a list of n primes
	primes = [2]
	k = 3
	while len(primes) < n:
		s = int(k**0.5)
		for p in primes:
			if p > s:
				primes.append(k)
				break
			if k % p == 0:
				break
		else:
			primes.append(k)
		k += 1
	return primes

primes = set(prime_list(10**4))
max_n, max_ab = 0, (0, 0)
for a, b in product(range(-999, 1000), range(-999, 1000)):
	f = lambda n: n**2 + a*n + b
	n = 0
	while f(n) in primes:
		n += 1
	if n > max_n:
		max_n, max_ab = n, (a, b)
print(max_n, max_ab)
print(max_ab[0]*max_ab[1])
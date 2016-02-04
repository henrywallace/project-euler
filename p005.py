"""The largest prime in [1, 20] is bounded by 20. We can quickly sieve up to 20, to get primes, and then ask what is the largest power of each of those primes? We then take the product of those."""

from math import log

def sieve(bound):
	if bound < 2:
		return []
	primes = [2]
	for n in range(3, bound):
		if not any(n % p == 0 for p in primes):
			primes.append(n)
	return primes

prod = 1
for p in sieve(20):
	prod *= p**int(log(20, p))
print(prod)
"""First find the maximum possible number of consecutive primes k, starting with the first prime. Then slide it over the primes to see if it works as a sum. If we ever exceed the largest prime, reduce k, and start from the first prime again."""

def sieve(bound):
	if bound < 2:
		return []
	primes = [2]
	for k in range(3, bound, 2):
		s = int(k**0.5) + 1
		for p in primes:
			if p > s:
				primes.append(k)
				break
			if k % p == 0:
				break
		else:
			primes.append(k)
	return primes

# first find largest possible k
primes = sieve(10**6)
pool = set(primes)
s, k = 0, 0
while s < primes[-1]:
	s += primes[k]
	k += 1

# now proceed to slide until sum exceeds largest prime
t, i = s, 0
while True:
	if s in pool:
		print(s)
		break
	elif s > primes[-1]:
		s = t - primes[k - 1]
		k -= 1
		t, i = s, 0
	else:
		s += primes[i + k] - primes[i]
		i += 1



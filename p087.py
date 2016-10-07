def sieve(bound):
    if bound < 2: return []
    primes = [2]
    for k in range(3, bound, 2):
        s = int(k**0.5)
        for p in primes:
            if p > s:
                primes.append(k)
                break
            elif k % p == 0:
                break
    return primes

bound = 50*10**6
primes = sieve(int((bound - 2**4 - 2**3)**0.5))
expressible = set()
for i in range(len(primes)):
    for j in range(len(primes)):
        for k in range(len(primes)):
            n = primes[i]**2 + primes[j]**3 + primes[k]**4
            if n > bound:
                break
            expressible.add(n)
print(len(expressible))

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

bound = 10**4
primes = set(sieve(bound))
possible = set()
for p in primes:
    for n in range(1, bound):
        possible.add(p + 2*n**2)
impossible = []
for n in range(3, max(possible), 2):
    if n not in possible and n not in primes:
        impossible.append(n)
print(impossible[0])

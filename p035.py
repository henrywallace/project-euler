"""We simply use a sieve with a bound, and then calculate by brute force."""


def sieve(bound):
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
        k += 1
    return primes


def rotations(n):
    s = str(n)
    for i in range(len(s)):
        yield int(s[i:] + s[:i])

pool = sieve(10**6)
k = 0
for p in pool:
    if all(r in pool for r in rotations(p)):
        k += 1
print(k)

from collections import Counter


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
            elif k % p == 0:
                break
        else:
            primes.append(k)
    return primes


def is_perm(n, m):
    s, t = str(n), str(m)
    if len(s) != len(t):
        return False
    return Counter(s) == Counter(t)

bound = 10**7
primes = sieve(bound)
x, m = 0, float('inf')
for p in primes:
    for q in primes:
        n = p*q
        if n > bound:
            break
        t = (p - 1)*(q - 1)
        if is_perm(n, t):
            r = n/t
            if r < m:
                x, m = n, r
print(x, m)

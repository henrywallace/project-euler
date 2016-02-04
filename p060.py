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
        else:
            primes.append(k)
    return primes

from itertools import combinations, permutations, starmap

concat = lambda *strs: ''.join(strs)

primes = set(map(str, sieve(1000)))
for s in combinations(primes, 5):
    if all(concat(*t) in primes for t in permutations(s, 2)):
        print(s)
        break
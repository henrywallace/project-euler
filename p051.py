from itertools import combinations

def sieve(bound):
    # bound exclusive
    primes, sieve = [], [True]*bound
    for i in range(2, bound):
        if sieve[i]:
            primes.append(i)
            for j in range(i**2, bound, i):
                sieve[j] = False
    return primes

def digit_replace(s, ind, r):
    return ''.join(r if i in ind else x for i, x in enumerate(s))

primes = list(map(str, sieve(10**6)))   # up to 6 digits primes
s = set(primes)
for p in primes:
    for k in range(1, 5):   # up to 4 digits replaced
        for ind in combinations(range(len(p)), k):
            t = []
            for r in map(str, range(10)):
                q = digit_replace(p, ind, r)
                if q in s:
                    t.append(q)
                if len(t) == 8:
                    print(t)
                    exit()
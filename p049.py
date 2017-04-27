"""
We'll create a set of 4 digit primes, and then go through all arithmetic
sequences. Let p be the smallest 4 digit prime. Then we want p + 2x < 10**4.
That is, we can bound our arithmetic increase by (10**4 - p)//2.
"""

from collections import Counter
from itertools import islice


def are_permuations(*nums):
    num_strs = [str(n) for n in nums]
    return all(Counter(a) == Counter(b) for a, b in
               zip(num_strs, islice(num_strs, 1, None)))

primes = [2]
k = 3
while k < 10**4:
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

primes = [p for p in primes if 10**3 <= p < 10**4]
pool = set(primes)

special = []
for x in range(1, (10**4 - primes[0])//2 + 1):
    for p in primes:
        series = [p + i*x for i in range(3)]
        if all(t in pool for t in series) and are_permuations(*series):
            special.append(series)
            print(series)
print(''.join(map(str, special[1])))

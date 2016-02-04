from functools import reduce
from operator import mul

fact = lambda n: reduce(mul, range(1, n + 1), 1)
factorials = {d: fact(d) for d in range(10)}

def fact_sum(n):
    s = 0
    while n > 0:
        d = n % 10
        s += factorials[d]
        n //= 10
    return s

def memoize(func):
    seen = {}
    def wrapper(*args):
        if args not in seen:
            seen[args] = func(*args)
        return seen[args]
    return wrapper

def chain_len(n):
    seen = set()
    @memoize
    def recur(x):
        if x in seen:
            return 0
        seen.add(x)
        return 1 + recur(fact_sum(x))
    return recur(n)

k = 0
for n in range(10**6):
    if chain_len(n) == 60:
        k += 1
print(k)
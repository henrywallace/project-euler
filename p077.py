def memoize(func):
    seen = {}

    def wrapper(*args):
        if args not in seen:
            seen[args] = func(*args)
        return seen[args]

    return wrapper


def npartitions(n, pool):

    @memoize
    def recur(x, i):
        if x == 0:
            return 1
        elif x < 0 or i == len(pool):
            return 0
        else:
            return recur(x - pool[i], i) + recur(x, i + 1)

    return recur(n, 0)


def primes():
    yield 2
    primes = [2]
    k = 3
    while True:
        s = int(k**0.5)
        for p in primes:
            if p > s:
                primes.append(k)
                yield k
                break
            elif k % p == 0:
                break
        k += 2

ps = primes()
pool = [next(ps)]
n = 1
while npartitions(n, pool) < 5000:
    n += 1
    if n > pool[-1]:
        pool.append(next(ps))
print(n, npartitions(n, pool))
print(pool)

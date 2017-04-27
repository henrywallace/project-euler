import heapq


def sieve(bound):
    if bound < 2:
        return []

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

# find upper bound on number of primes in heap
x = 15499/94744
primes = sieve(10**2)
t = 1
for i, p in enumerate(primes):
    t *= 1 - 1/p
    if t < x:
        break

primes = primes[:i]
# x = 4/10
heap = [(1, 1, set())]
for _ in range(10**6):
    n, t, s = heapq.heappop(heap)
    for p in primes:
        if p in s:
            heapq.heappush(heap, (n*p, t*p, s))
        else:
            r = s.copy()
            r.add(p)
            heapq.heappush(heap, (n*p, t*(p - 1), r))
    if n > 1 and t/(n - 1) < x:
        print(n)
        break

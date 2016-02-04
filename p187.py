"""
primes below 30//2 are
2 3 5 7 11 13

6 + 3 + 1
"""

def sieve(bound):
    primes, sieve = [], [True]*(bound + 1)
    for p in range(2, bound + 1):
        if sieve[p]:
            primes.append(p)
            for i in range(p**2, bound + 1, p):
                sieve[i] = False
    return primes

def index(a, n):
    # binary search to return index of largest p in a <= n
    def recur(lo, hi):
        if lo >= hi:
            return lo
        mid = (lo + hi)//2 + 1
        if a[mid] <= n:
            return recur(mid, hi)
        else:
            return recur(lo, mid - 1)
    return recur(0, len(a) - 1)

bound = 31
primes = sieve(13)
print(primes)
# count = 0
# for i, p in enumerate(primes):
#     if p**2 > bound:
#         break
#     j = index(primes, bound//p)
#     count += j - i + 1
# print(count)
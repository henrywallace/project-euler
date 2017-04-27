from itertools import chain


def nfactors(n):
    # output number of distinct prime factors
    s = 0
    for d in chain([2], range(3, int(n**0.5) + 1, 2)):
        if n % d == 0:
            s += 1
            while n % d == 0:
                n //= d
        if n == 1:
            return s
    if n > 1:
        return s + 1

n = 1
while True:
    k = 0
    while nfactors(n) == 4:
        k += 1
        if k == 4:
            print(n - 3, n - 2, n - 1, n)
            exit()
        n += 1
    n += 1

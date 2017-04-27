from itertools import chain


def phi(n):
    t = n
    for d in chain([2], range(3, int(n**0.5) + 1, 2)):
        if n % d == 0:
            t *= 1 - 1/d
            while n % d == 0:
                n //= d
            if n == 1:
                return t
    if n > 1:
        t *= 1 - 1/n
    return t

print(max((n/phi(n), n) for n in range(1, 10**6 + 1)))

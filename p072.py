from itertools import chain

def phi(n):
    t = n
    for d in chain([2], range(3, int(n**0.5) + 1, 2)):
        if n % d == 0:
            t *= 1 - 1/d
            while n % d == 0:
                n //= d
            if n == 1:
                return int(round(t))
    if n > 1:
        t *= 1 - 1/n
    return int(round(t))

print(sum(map(phi, range(2, 10**6 + 1))))
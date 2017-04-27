from itertools import chain


def largest_factor(n):
    """Simple trial factorization, with keeping maximum."""
    l = 0		# largest factor
    for d in chain([2], range(3, int(n**0.5) + 1, 2)):
        while n % d == 0:
            n //= d
            l = d
        if n == 1:
            break
    if n > 1:
        l = max(l, n)
    return l


print(largest_factor(600851475143))

'''Project Euler Problem 203

The function `squarefree_binomials` yields distinct squarefree binomials. This
is done by inspecting each binomial's prime factorization, and deduping.

We compute the factorization of each row number, remembering each
factorizations, and the primes among the way.

TODO: What's the runtime? Specifically, what's the complexity of factorization,
with a list of primes?

'''
from collections import Counter
from itertools import count
from math import sqrt


def iter_factors(start=2):
    '''Yield prime factorizations for successive integers starting at `start`.

    Each factorizationss is represented by a `Counter`, whose keys are primes,
    and whose values are corresponding exponents. Note that 1 then has
    factorization `Counter()`.

    Yields:
        `Counter`s, representing factorizations, whose keys are primes, and
        whose values are corresponding exponents.

    '''
    assert start > 0 and isinstance(start, int)

    primes = []  # primes will be kept in sorted order

    for n in count(start):
        factors = Counter()

        bound = int(sqrt(n))  # since at minimum `n` = (some prime)^2
        for p in primes:
            if p > bound:
                break
            while n % p == 0:
                n //= p
                factors[p] += 1

        if n > 1:  # then n is prime
            factors[n] = 1
            if not primes or n > primes[-1]:  # skip primes we've seen before
                primes.append(n)

        yield factors


def squarefree_binomials(num_rows):
    '''Yields distinct squarefree binomials from the first `num_rows` rows.

    Distinct squarefree binomials are yielded in the order it would have first
    been seen in row-major order.

    Args:
        num_rows: Number of rows to iterate over, starting at 0.
    Yields:
        Distinct squarefree binomials in row-major order, stopping at column
        n//2 + 1.

    '''
    yield 1
    seen = {1}

    factorizations = {}

    # loop over n, k starting from row 1
    for n, factors in zip(range(1, num_rows), iter_factors(start=1)):
        factorizations[n] = factors

        for k in range(1, n//2 + 1):  # since (n, k) == (n - k, k)
            factors = Counter()
            for m in range(n - k + 1, n + 1):  # n! / (n - k)!
                factors += factorizations[m]
            for m in range(2, k + 1):          # k!
                factors -= factorizations[m]

            binomial = 1   # construct the binomial from its factorization
            for p, e in factors.items():
                if e > 1:  # divisible by a square
                    break
                binomial *= p**e
            else:
                if binomial not in seen:
                    seen.add(binomial)
                    yield binomial


if __name__ == '__main__':
    print(sum(squarefree_binomials(8)))
    print(sum(squarefree_binomials(51)))

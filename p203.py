'''Project Euler Problem 203

We yield squarefree binomials from `squarefree_binomials`. This is done by
inspecting each binomial's prime factorization.

While we iterate over Pascal's Triangle's rows, we save each new integer's
factorization, computing successive factorizations from previous integers'.

The function `iter_factors` yields factorizations successive integers starting
at `start=0`.

Note that `squarefree_binomials` could be optimized more by first yielding 1,
and iterating `k` over `range(1, n//2 + 1)`, since I thought it muddled things.

'''
from collections import Counter
from itertools import count, islice


def iter_factors(start):
    '''Yield prime factorizations for successive integers starting at `start`.

    Yields:
        Tuples of `(n, factors)`, where `factors` is a Counter whose keys
        are primes, and whose values are the exponents of those primes in `n`'s
        factorization.

    '''
    primes = []

    for n in count(start):
        m = n
        factors = Counter()
        
        for p in primes:
            while m % p == 0:
                m //= p
                factors[p] += 1

        if not factors and n > 1:  # then n is prime
            primes.append(n)
            factors = Counter({n: 1})

        yield n, factors


def squarefree_binomials(num_rows):
    '''Yield squarefree binomials from the first `num_rows` rows.

    Only the first n//2 + 1 columns of each row are iterated over.

    Args:
        num_rows: Number of rows to iterate over, starting at 0.
    Yields:
        Squarefree binomials in row-major order, stopping at column n//2 + 1.

    '''
    factorizations = {}
    
    for n, factors in islice(iter_factors(start=0), num_rows):
        factorizations[n] = factors
        
        for k in range(n//2 + 1):  # since (n, k) == (n - k, k)
            if k == 0 or k == n:   # boundary values are squarefree
                yield 1
                continue

            factors = Counter()
            for m in range(n - k + 1, n + 1):  # n! / (n - k)!
                factors += factorizations[m]
            for m in range(2, k + 1):          # k!
                factors -= factorizations[m]
                
            binomial = 1
            for p, e in factors.items():
                if e > 1:
                    break
                binomial *= p**e
            else:
                yield binomial


def distinct_sum(num_rows):
    '''Return the sum of distinct squarefree numbers from the first `num_rows`
    rows.

    '''
    return sum(set(squarefree_binomials(num_rows)))


if __name__ == '__main__':
    print(distinct_sum(8))
    print(distinct_sum(51))

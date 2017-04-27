"""
Naively eyeball the upperbound 10**4. But we only need a small set of
solutions, and then take the smallest. This is because P(n) - P(n - 1)
is increasing in n.
"""

from itertools import combinations

pentagonals = set(n*(3*n - 1)//2 for n in range(1, 10**4))
for n, m in combinations(pentagonals, 2):
    if n + m in pentagonals and abs(n - m) in pentagonals:
        print(n, m, abs(n - m))

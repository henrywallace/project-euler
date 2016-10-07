from fractions import Fraction
from functools import lru_cache

def nsols():
    pool = [Fraction(1, n**2) for n in range(2, 20)]
    @lru_cache()
    def recur(x, i):
        if x == 0:
            return 1
        elif x < 0 or i == len(pool):
            return 0
        else:
            return recur(x - pool[i], i + 1) + recur(x, i + 1)
    return recur(Fraction(1, 2), 0)

print(nsols())
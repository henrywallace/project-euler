from fractions import Fraction

def memoize(func):
    seen = {}
    k = 0
    def wrapper(*args):
        if args not in seen:
            seen[args] = func(*args)
        else:
            k += 1
            print(k)
        return seen[args]
    return wrapper

def nsols():
    pool = [Fraction(1, n**2) for n in range(2, 20)]
    @memoize
    def recur(x, i):
        if x == 0:
            return 1
        elif x < 0 or i == len(pool):
            return 0
        else:
            return recur(x - pool[i], i + 1) + recur(x, i + 1)
    return recur(Fraction(1, 2), 0)

print(nsols())
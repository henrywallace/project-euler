def memoize(func):
    seen = {}
    def wrapper(*args):
        if args not in seen:
            seen[args] = func(*args)
        return seen[args]
    return wrapper

def nways(n):
    @memoize
    def recur(x, color, nblack):
        if x < 0 or nblack < 0:
            return 0
        elif x == 0:
            return 1
        else:
            return recur(x - color, color, nblack) + \
                    recur(x - 1, color, nblack - 1)
    return sum(recur(n, color, n - 1) \
        for color in [2, 3, 4])

print(nways(50))
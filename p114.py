def memoize(func):
    seen = {}
    def wrapper(*args):
        if args not in seen:
            seen[args] = func(*args)
        return seen[args]
    return wrapper

def nways(n):
    @memoize
    def recur(x, prev_red):
        if x == 0:
            return 1
        elif x < 0:
            return 0
        elif prev_red:
            return recur(x - 1, False)
        else:
            return recur(x - 1, False) + \
                    sum(recur(x - t, True) for t in range(3, n + 1))
    return recur(n, False)

print(nways(50))
def memoize(func):
    seen = {}
    def wrapper(*args):
        if args not in seen:
            seen[args] = func(*args)
        return seen[args]
    return wrapper

def nways(n):
    tiles = [1, 2, 3, 4]
    @memoize
    def recur(x):
        if x == 0:
            return 1
        elif x < 0:
            return 0
        else:
            return sum(recur(x - t) for t in tiles)
    return recur(n)

print(nways(50))
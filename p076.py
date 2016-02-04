def memoize(f):
    seen = {}
    def decorator(*args):
        if args not in seen:
            seen[args] = f(*args)
        return seen[args]
    return decorator

def nsums(n):
    a = list(range(1, n))
    @memoize
    def recur(n, i):
        if n == 0:
            return 1
        elif n < 0 or i == len(a):
            return 0
        else:
            return recur(n - a[i], i) + recur(n, i + 1)
    return recur(n, 0)

print(nsums(100))
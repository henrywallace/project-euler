def lagrange_interp(xs, ys):
    xs, ys = map(list, (xs, ys))

    def func(a):
        ans = 0
        for i, y in enumerate(ys):
            t = y
            for j, x in enumerate(xs):
                if i == j:
                    continue
                t *= (a - x)/(xs[i] - x)
            ans += t
        return ans

    return func

u = lambda n: sum((-1)**i * n**i for i in range(11))
# u = lambda n: n**3

s = 0
ys = []
for k in range(1, 10 + 1):
    ys.append(u(k))
    f = lagrange_interp(range(1, k + 1), ys)
    s += f(k + 1)
print(round(s))

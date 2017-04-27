from itertools import count

tn = lambda n: n*(n + 1)//2
pn = lambda n: n*(3*n - 1)//2
hn = lambda n: n*(2*n - 1)

k = 0
tg, pg, hg = (map(f, count(1)) for f in (tn, pn, hn))
t, p, h = map(next, (tg, pg, hg))
while k < 3:
    if t == p == h:
        print(t)
        t, p, h = map(next, (tg, pg, hg))
        k += 1
    while h > p:
        p = next(pg)
    while p > t:
        t = next(tg)
    while p > h:
        h = next(hg)

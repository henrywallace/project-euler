from math import log10

s = 0
for n in range(1, 101):
    for r in range(0, n + 1):
        t = 0 - sum(map(log10, range(1, r + 1)))
        a = n
        for _ in range(r):
            t += log10(a)
            a -= 1
            if t > 6:
                s += 1
                break
print(s)
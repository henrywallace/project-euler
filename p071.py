t, bound = 3/7, 10**6
a, b = 1, bound
x = a/b
for d in range(1, bound + 1):
    for n in range(max(1, int(x*d)), bound + 1):
        y = n/d
        if y >= t:
            break
        elif y > x:
            a, b, x = n, d, y

print(a, b, x)

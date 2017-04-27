def min_x(d):
    y = 1
    while True:
        t = 1 + d*(y**2)
        s = int(t**0.5)
        if s**2 == t:
            return s
        elif (s + 1)**2 == t:
            return s + 1
        y += 1

squares = set(n**2 for n in range(32))
# print(max(map(min_x, set(range(2, 8)) - squares)))
for d in set(range(2, 1001)) - squares:
    print(d, min_x(d))

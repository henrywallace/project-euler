def nsols(p):
    n = 0
    for a in range(1, p - 1):
        for b in range(a, p - a):
            for c in range(1, p - a - b + 1):
                if a + b + c == p and a**2 + b**2 == c**2:
                    n += 1
    return n

print(max((nsols(p), p) for p in range(1, 1001)))

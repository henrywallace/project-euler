def cycle_len(n, d):
    # method by long division
    quot = {}
    k = 0
    while True:
        if n in quot:
            return k - quot[n]
        if n < d:
            n *= 10
            k += 1
            continue
        quot[n] = k
        n %= d
        if n == 0:
            return 0

print(max((cycle_len(1, d), d) for d in range(1, 999)))
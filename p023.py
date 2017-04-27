def is_abundant(n):
    if n == 1:
        return False
    s = 0
    for d in range(1, int(n**0.5) + 1):
        if n % d == 0:
            s += d
            if d != 1 and n//d != d:
                s += n//d
    return s > n

abundants = list(filter(is_abundant, range(1, 28123 + 1)))
pool = set(abundants)
s = 0
for n in range(1, 28123 + 1):
    for a in abundants:
        if a > n:
            s += n
            break
        if n - a in pool:
            break
    else:
        s += n
print(s)

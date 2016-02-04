def pandigital(num_str):
    seen = set()
    for c in num_str:
        if c in seen or c == '0':
            return False
        seen.add(c)
    return len(seen) == 9

prev, curr, n = 0, 1, 1
while True:
    print(n)
    prev, curr = curr, prev + curr
    n += 1
    s = str(curr)
    if pandigital(s[-9:]) and pandigital(s[:9]):
        print(n, s)
        break
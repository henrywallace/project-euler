def primes():
    # endless generator of primes
    yield 2
    primes = [2]
    k = 3
    while True:
        s = int(k**0.5) + 1
        for p in primes:
            if p > s:
                primes.append(k)
                yield k
                break
            if k % p == 0:
                break
        else:
            primes.append(k)
            yield k
        k += 1


def is_pandigital(n):
    s = str(n)
    seen = set()
    for c in s:
        if any((c == '0', int(c) > len(s), c in seen)):
            return False
        seen.add(c)
    return True

m = 0
for p in primes():
    if p > 10**7:  # since 3 divides > 7 digit pandigital numbers
        break
    if is_pandigital(p) and p > m:
        m = p
print(m)

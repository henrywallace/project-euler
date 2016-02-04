def prime_list(n):
    if n < 1: return []
    primes = [2]
    k = 3
    while len(primes) < n:
        s = int(k**0.5)
        for p in primes:
            if p > s:
                primes.append(k)
                break
            elif k % p == 0:
                break
        else:
            primes.append(k)
        k += 1
    return primes

primes = prime_list(6)
n = 2
while True:
    ndiv = 1
    m = n
    for p in primes:
        k = 0
        while m % p == 0:
            k += 1
            m //= p
            if m == 1:
                break
        ndiv *= 2*k + 1
    else:
        if m == 1 and ndiv > 2000:
            print(n, ndiv)
            break
    n += 1
def prime(n):
    primes = [2]
    k = 3  # next prime candidate
    while n > 1:
        s = int(k**0.5)
        for p in primes:
            if p > s:
                primes.append(k)
                n -= 1
                break
            if k % p == 0:
                break
        else:
            primes.append(k)
            n -= 1
        k += 2
    return primes[-1]


print(prime(10001))

def prime_sum(bound):
    primes = [2]
    k = 3
    while k < bound:
        s = int(k**0.5)
        for p in primes:
            if p > s:
                primes.append(k)
                break
            if k % p == 0:
                break
        else:
            primes.append(k)
            break
        k += 2
    return sum(primes)

print(prime_sum(2*10**6))

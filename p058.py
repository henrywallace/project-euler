from random import randint

def is_prime(n, trials=16):
    # rabin miller primality test
    assert(n > 1)
    if n == 2: return True
    l, m = 0, n - 1
    while m % 2 == 0:
        m //= 2
        l += 1
    for _ in range(trials):
        a = randint(2, n - 1)
        x = pow(a, m, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(l - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
            if x == 1:
                return False
        else:
            return False
    return True

n, s = 1, 2
nprime, ndiag = 0, 1
while nprime/ndiag > 0.1 or nprime == 0:
    for _ in range(4):
        n += s
        if is_prime(n):
            nprime += 1
    ndiag += 4
    s += 2
print(s - 1)
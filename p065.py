def e_terms():
    i, k = 0, 1
    while True:
        if i == 1:
            yield 2*k
            k += 1
        else:
            yield 1
        i += 1
        i %= 3

def frac_approx(k, init, terms):
    assert(k > 0)
    if k == 1:
        return init
    terms = iter(terms)     # to allow recursion with `next`
    def recur(j):
        if j == 0:
            return (0, 1)
        try:        # in case terms isn't infinite...
            t = next(terms)
            (n, d) = recur(j - 1)
            return (d, t*d + n)
        except StopIteration:
            raise
    n, d = recur(k - 1)
    return (init*d + n, d)

(n, d) = frac_approx(100, 2, e_terms())
print(sum(int(x) for x in str(n)))


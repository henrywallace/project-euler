"""
The difference between consecutive positive pentagonals is 3k + 1, whereas for
negative it's 3*(-k) + 2. We then only need to pay attention to the parity of
the length of generalized pentagonal list, and append appropriately. If the
parity is even, then the next number we add will be a positive one, etc.
However there's a hack, 2 + 3*(len(g)//2) = 1 + (3*len(g))//2 whenever parity
is odd; so we don't even need to check parity!
"""

p = [1, 1]      # p(0) = p(1) = 1
g = [1, 2]      # generalized pentagonals, n = 1, -1
n = 1
while p[-1] % 10**6 != 0:
    n += 1
    if g[-1] < n:
        g.append(g[-2] + 1 + (3*len(g))//2)
    p_next = 0
    for i, x in enumerate(g):
        if x > n:
            break
        if i % 4 == 0 or i % 4 == 1:
            p_next += p[n - x]
        else:
            p_next -= p[n - x]
    p.append(p_next)
print(n, p[-1])

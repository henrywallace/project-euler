"""Note that the number of rectangles in a grid of r rows and c columsn is Sum[Sum[(r - i + 1) (c - j + 1), {j, 1, c}], {i, 1, r}] = Sum[Sum[i j, {j, 1, c}], {i, 1, r}] = tri(c)*tri(r) = c(1 + c)r(1 + r)/4."""

def nrecs(r, c):
    return r*(r + 1)*c*(c + 1)//4

m, mr, mc = float('inf'), 0, 0
for r in range(1, 10**5):
    for c in range(1, 10**5):
        n = nrecs(r, c)
        d = abs(n - 10**6)
        if d < m:
            print(m)
            m, mr, mc = d, r, c
        break
print(m, mr, mc, nrecs(mr, mc))
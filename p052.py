from collections import Counter

def is_permuted(n, m):
    s, t = str(n), str(m)
    if len(s) != len(t):
        return False
    return Counter(s) == Counter(t)

# simple brute force
n = 1
while True:
    if all(is_permuted(n, k*n) for k in range(2, 7)):
        print(n, 2*n, 3*n, 4*n, 5*n, 6*n)
        break
    n += 1
s = 0
for n in range(1, 1000 + 1):
    s += pow(n, n, 10**10)
    s %= 10**10
print(s)

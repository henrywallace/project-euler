def gcd(a, b):
    while b > 0:
        a, b = b, a%b
    return a

lower = 1/3
upper = 1/2
s = 0

for d in range(5, 12000 + 1):
    for n in range(int(lower*d) + 1, int(upper*d) + 1):
        if gcd(n, d) == 1:
            s += 1
print(s)
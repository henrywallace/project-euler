def is_square(n):
    s = int(n**0.5)
    if s**2 == n:
        return s
    elif (s + 1)**2 == n:
        return s + 1
    else:
        return -1

# find the solution
n = 10**12
while True:
    for i in range(2):
        n += i
        x = 4 + 8*n*(n - 1)
        s = is_square(x)
        if s > 0:
            print(n, s)
    n += 4

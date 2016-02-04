n = 1
while True:
    if n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
        n += 1
        continue
    else:
        if pow(10, 10**6 + 1, n) == 1:
            print(n)
            break
        n += 1
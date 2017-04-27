def palindromic(n):
    s = str(n)
    for i in range(len(s)//2):
        if s[i] != s[-(i + 1)]:
            return False
    return True


l = 0
for n in range(1, 10**3):
    for m in range(n, 10**3):
        prod = n*m
        if palindromic(prod):
            l = max(prod, l)
print(l)

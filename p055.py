def reverse_add(n):
    return n + int(str(n)[::-1])

def is_palindrome(n):
    s = str(n)
    for i in range(len(s)//2):
        if s[i] != s[-(i + 1)]:
            return False
    return True

def is_lychrel(n):
    for _ in range(50):
        n = reverse_add(n)
        if is_palindrome(n):
            return False
    return True

k = 0
for n in range(10**4):
    if is_lychrel(n):
        k += 1
print(k)

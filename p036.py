def palindrome(s):
    return all(s[i] == s[-(i + 1)] for i in range(len(s)//2))

s = 0
for n in range(10**6):
    if palindrome(str(n)) and palindrome(bin(n)[2:]):
        s += n
print(s)

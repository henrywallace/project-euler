from fractions import Fraction


def is_bouncy(n):
    inc = False
    dec = False
    prev, n = n % 10, n//10
    while n > 0:
        curr, n = n % 10, n//10
        if curr < prev:
            inc = True
        elif curr > prev:
            dec = True
        prev = curr
        if inc and dec:
            return True
    return False

nbouncy, n = 0, 1
while True:
    if is_bouncy(n):
        nbouncy += 1
    if Fraction(nbouncy, n) == Fraction(99, 100):
        print(n)
        break
    n += 1

# k = 0
# for n in range(539):
#     if is_bouncy(n):
#         k += 1
# print(2*k)

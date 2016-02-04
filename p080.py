from decimal import *

getcontext().prec = 102     # to get around rounding


squares = set(n**2 for n in range(1, 10))
s = 0
for n in range(1, 100):
    if n not in squares:
        digits = list(filter(str.isdigit, str(Decimal(n).sqrt())[:-2]))
        s += sum(map(int, digits))
print(s)
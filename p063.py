from math import log10, ceil

k = 0
for m in range(1, 21 + 1):
    k += 10 - ceil(pow(10, 1 - 1/m))
print(k)
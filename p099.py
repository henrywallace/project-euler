from math import log

i, m = 0, float('-inf')
with open('p099_base_exp.txt') as f:
    for j, line in enumerate(f.readlines(), start=1):
        b, e = map(int, line.split(','))
        x = e*log(b)
        if x > m:
            m = x
            i = j
print(i)

from itertools import permutations

divisors = [2, 3, 5, 7, 11, 13, 17]
pandigitals = []

for p in permutations(range(10)):
    if p[0] == 0:
        continue
    if all((100*p[i] + 10*p[i + 1] + p[i + 2]) % d == 0 \
            for i, d in enumerate(divisors, start=1)):
        pandigitals.append(int(''.join(map(str, p))))

print(pandigitals)
print(sum(pandigitals))
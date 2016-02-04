seen = {1: 1, 89: 89}
for n in range(1, 10**7 + 1):
    chain = set()
    while n != 1 and n != 89:
        if n in seen:
            break
        chain.add(n)
        n = sum(int(d)**2 for d in str(n))
    for x in chain:
        seen[x] = seen.get(n, n)

print(sum(1 for v in seen.values() if v == 89))
# print(seen)
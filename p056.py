# Python handles arbitrary precision, so this is easy
print(max(sum(map(int, str(a**b))) for a in range(100) for b in range(100)))

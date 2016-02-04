numer, denom = 1, 1
for d in range(10, 100):
	for n in range(10, d):
		if d % 10 == 0:
			continue
		ns, ds = str(n), str(d)
		if len(set(ns) & set(ds)) > 0:
			i = 0 if ns[0] in ds else 1
			if ns[i] == ds[0]:
				t = (ns[1 - i], ds[1])
			else:
				t = (ns[1 - i], ds[0])
			if int(t[0])/int(t[1]) == n/d:
				numer *= n
				denom *= d
				print(n, d)

def gcd(a, b):
	while b > 0:
		a, b = b, a % b
	return a

print(numer, denom)
print(denom//gcd(numer, denom))

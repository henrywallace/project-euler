from itertools import chain

def ndivisors(n):
	ndiv = 1
	for d in chain([2], range(3, int(n**0.5) + 1, 2)):
		k = 0
		while n % d == 0:
			n //= d
			k += 1
		ndiv *= k + 1
		if n == 1:
			return ndiv
	if n > 1:
		ndiv *= 2
	return ndiv

T = 1
k = 2
while True:
	if ndivisors(T) > 500:
		print(T)
		break
	T += k
	k += 1

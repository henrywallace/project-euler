from operator import mul
from functools import reduce

fact = lambda n: reduce(mul, range(1, n + 1))

def permutation(it, n):
	pool = list(it)
	m = len(pool)
	f = fact(m - 1)
	for k in range(m - 1, 1, -1):
		i, r = n//f, n%f
		if r == 0:
			n = f
			yield pool.pop(i - 1)
		else:
			n = r
			yield pool.pop(i)
		f //= k
	yield pool.pop()

print(int(''.join(map(str, permutation(range(10), 10**6)))))


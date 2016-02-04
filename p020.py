from functools import reduce
from operator import mul

print(sum(int(x) for x in str(reduce(mul, range(1, 11)))))
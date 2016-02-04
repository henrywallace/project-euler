"""We need not recourse to coding for this problem. Suppose we have an n x n grid; each time we can only go down or right. A total of n + n choices will be made. If we think about at what times we go right, then the downs will be determined. Thus the number of ways is simply 2n choose n."""

ans = 1
for i in range(20):
	ans *= 40 - i
for i in range(1, 21):
	ans //= i
print(ans)
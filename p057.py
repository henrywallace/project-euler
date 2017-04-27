"""
Note that 1 + 1/(2 + ...) = 1 + 1/(1 + (1 + 1/(2 + ...))) so that the problem
is self-similar. So I proceed by a simple loop.
"""

s = 0
n, d = 1, 1
for _ in range(10**3):
    n, d = d, n + d     # 1 + inverse of previous result
    n, d = n + d, d
    if len(str(n)) > len(str(d)):
        s += 1
print(s)
"""
Let x be side length of square hole, then lamina sizes are:
x=1: 3^2 - 1^2, 5^2 - 1^2, ...
x=2: 4^2 - 2^2, 6^2 - 2^2, ...
...
x=7: 9^2 - 7^2, 11^2 - 7^2, ...

In general: {(x + 2k)^2 - x^2 : k >= 1}
Upper bound is [(x + 2k)^2 - x^2 <= 10^6] so that
    k <= (sqrt(10^6 + x^2) - x)/2
    k <= O(x)
And the maximum x will be when it's smallest lamina size is exceeds 10^6.
So we have the bound, (x + 2)^2 - x^2 <= 10^6
                                    x <= 10^6/4 - 1
"""

bound = 10**6
t = 0
for x in range(1, bound//4):
    max_k = ((bound + x**2)**0.5 - x)/2
    for k in range(1, int(max_k) + 1):
        t += 1
print(t)
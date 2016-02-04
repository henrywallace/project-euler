"""This can be computed simply by combining formulas that can be obtained from induction. n^2(n + 1)^2/4 - n(n + 1)(2n + 1)/6 = (n - 1)n(n + 1)(3n + 2)/12"""

n = 10
print((n - 1)*n*(n + 1)*(3*n + 2)//12)
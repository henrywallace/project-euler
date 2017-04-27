"""
We expand each polynomials with the binomial theorem, and see that all powers
a^k, k > 2, are congruent to 0 modulo a^2. Howeveer, depending on the parity
of n (a - 1)^n + (a + 1)^n cancel out differently. When n is even,

(a - 1)^n + (a + 1)^n = sum k=0..n { binom(n, k)*a^(n-k)*(1 + (-1)^k) }
                      = 2  mod a^2

Otherwise, when n is odd, then

                      = 2*binom(n, 1)*a  mod a^2
                      = 2*n*a  mod a^2

And since gcd(a, a^2) = a,

      2*n*a  mod a^2 <=> 2*n  mod a

And when a is even, gcd(2, a) = 2 so that

    2*n  mod a <=> n  mod a/2

Clearly the maximum occurs at one less then the modulus, and will persist with
the cancellation since it's only scaling. The maximum is n = (a - 1)/2 or
a/2 - 1 depending on the parity. In both cases it's equivalent to (a - 1)//2.
"""

from math import floor

print(sum(2*a*floor((a - 1)/2) for a in range(3, 1001)))

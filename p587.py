"""
Consider the bottom-left corner of the L-section to be the origin of a
cartesian coordinate system. We can draw a unit circle for n = 1 with

    (x - 1)^2 + (y - 1)^2 = 1       [1]

For any n, the line from the origin to the top-right most corner of the
rectangle is simply

    2/(2n) * x = x/n                [2]

Let t denote the x coordinate at which this line intersects the circle. We can
find the area concave triange by summing its left and right part, divided by x
= t. That is, the sum of integrating the line x/n from 0 to t, and integrating
the lower belly of the circle from t to 1.

Given our cartesian setup, the area of the L-section is just

    2^2 - pi * 1^2 = 1 - pi/4       [3]

From here, the details from here are straightforward. Now, while I could have
solved this whole thing by hand, I got tired trying to figure out the
integral. So, here I find myself using scipy...
"""
from itertools import count
from math import pi, sqrt

from scipy import integrate

L = 1 - pi/4  # see [3]


def tip(n):
    """
    The x coordinate at which the line intersects the concave triange.

    If we plug [1] into [2], then we get a quadratic. And since the line
    intersects the circle at its lower-left _and then_ its upper right, we
    take the smaller solution.
    """
    a = (1/n**2 + 1)
    b = -2*(1/n + 1)
    c = 1
    return (-b - sqrt(b**2 - 4*a*c))/(2*a)


def area(n):
    """
    Compute the area of the concave triangle by summing two parts.

    The two parts are divided by the line x = t. The right part is difficult,
    so we use a numerical approximation. But the left side is easy.
    """
    t = tip(n)
    left = t**2/(2*n)
    circle = lambda x: 1 - sqrt(1 - (x - 1)**2)
    right = integrate.quad(circle, t, 1)[0]
    return left + right


if __name__ == '__main__':
    for n in count(1):
        ratio = area(n)/L
        if ratio < 0.001:
            print(n, ratio)
            break

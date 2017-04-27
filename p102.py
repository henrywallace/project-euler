from math import acos, hypot, pi


def angle(u, v):
    # angle between vectors u and v
    dot = sum(a*b for a, b in zip(u, v))
    return acos(dot/hypot(*u)/hypot(*v))


def vector(p1, p2):
    # vector from coordiates p1 to p2
    return tuple(b - a for a, b in zip(p1, p2))


def inside_triangle(p, a, b, c):
    # sum of angles between (p, a), (p, b), (p, c) should be 2*pi
    u, v, w = vector(p, a), vector(p, b), vector(p, c)
    alpha = angle(u, v) + angle(u, w) + angle(v, w)
    return abs(2*pi - alpha) < 1e-6

k = 0
with open('p102_triangles.txt') as f:
    for line in f.readlines():
        numbers = [int(x) for x in line.strip().split(',')]
        a, b, c = numbers[0:2], numbers[2:4], numbers[4:6]
        if inside_triangle((0, 0), a, b, c):
            k += 1
print(k)

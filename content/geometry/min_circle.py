from random import shuffle
from math import sqrt
from twod import sub, abs_squared, cross, add, mult
# Finds the minimum enclosing circle of a group of points as represented by tuples
# Returns center coordinates, radius
# Algorithm sourced from waynedisonitau123 & converted to python
def center(a, b, c):
    p0 = sub(b, a)
    p1 = sub(c, a)
    c1 = abs_squared(p0) * 0.5
    c2 = abs_squared(p1) * 0.5
    d = cross(p0, p1)
    x = a[0] + (c1 * p1[1] - c2 * p0[1]) / d
    y = a[1] + (c2 * p0[0] - c1 * p1[0]) / d
    return x, y
def solve(p):
    shuffle(p)
    r = 0.0
    cent = (0, 0)
    for i in range(len(p)):
        if abs_squared(sub(cent, p[i])) <= r:
            continue
        cent = p[i]
        r = 0.0
        for j in range(i):
            if abs_squared(sub(cent, p[j])) <= r:
                continue
            cent = mult(add(p[i], p[j]), 1/2)
            r = abs_squared(sub(p[j], cent))
            for k in range(j):
                if abs_squared(sub(cent, p[k])) <= r:
                    continue
                cent = center(p[i], p[j], p[k])
                r = abs_squared(sub(p[k], cent))
    return cent, sqrt(r)
from math import sqrt
def add(a, b):
    return a[0] + b[0], a[1] + b[1]
def sub(a, b):
    return a[0] - b[0], a[1] - b[1]
def opp(a):
    return -a[0], -a[1]
def mult(a, s):
    return a[0] * s, a[1] * s
def abs(a):
    return sqrt(a[0] * a[0] + a[1] * a[1])
def abs_squared(a):
    return a[0] * a[0] + a[1] * a[1]
def dist(a, b):
    return abs(sub(a, b))
def dot(a, b):
    return a[0] * b[0] + a[1] * b[1]
def cross(a, b):
    return a[0]*b[1] - a[1]*b[0]
def cross3(a, b, c):
    return cross(sub(c, a), sub(c, b))

# Do segments AB and CD intersect
def intersects(a, b, c, d):
    if cross3(b, c, a) * cross3(b, d, a) > 0: return False
    if cross3(d, a, c) * cross3(d, b, c) > 0: return False
    return True

# Get intersection of segments AB and CD
def intersectPoint(a, b, c, d):
    x, y = cross3(b, c, a), cross3(b, d, a)
    if x == y: pass # handle is parallel
    else: return sub(mult(d, (x/(x-y))), mult(c, (y/(x-y))))
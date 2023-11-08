# Find max/min of unimodal func on interval [l, r]
def ternary_search(f, l, r, eps=1e-9):
    while abs(r - l) > eps:
        m1 = l + (r - l) / 3
        m2 = r - (r - l) / 3
        # > = min, < = max
        if f(m1) < f(m2):
            l = m1
        else:
            r = m2
    return (l + r) / 2
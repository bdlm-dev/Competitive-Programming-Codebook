from math import gcd
# gcd of multiple numbers:
def gcd_m(lst):
    if len(lst) == 0:
        return 999999 # no gcd
    elif len(lst) == 1:
        return lst[0]
    out = gcd(lst[0], lst[1])
    for i in range(2, len(lst)):
        out = gcd(out, lst[i])
    return out
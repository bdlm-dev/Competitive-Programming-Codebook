# integer factorization
def pollard_rho(n):
    if n == 1: return 1
    f = lambda x: (x * x + 1) % n
    x, y, d = 2, 2, 1
    while d == 1:
        x = f(x)
        y = f(f(y))
        d = gcd(abs(x - y), n)
    if d == n:
        return pollard_rho(n)
    return d
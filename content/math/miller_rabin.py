# probability-based primality test- >k more accurate, slower
def miller_rabin(n, k=5):
    if n < 4: return n == 2 or n == 3
    if n % 2 == 0: return False
    d, r = n - 1, 0
    while d % 2 == 0:
        d, r = d // 2, r + 1
    def witness(a):
        x = pow(a, d, n)
        if x == 1 or x == n - 1: return True
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1: return True
        return False
    return all(witness(random.randint(2, min(n - 2, 2 + int(2 * (pow(n.bit_length(), 2)) ** 0.5)))) for _ in range(k))

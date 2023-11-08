def sieve_of_eratosthenes(n):
    primes, p = [True for _ in range(n+1)], 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    return [i for i in range(2, n + 1) if primes[i]]
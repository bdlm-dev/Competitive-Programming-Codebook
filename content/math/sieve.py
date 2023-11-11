from math import ceil, sqrt
def sieve_of_eratosthenes(n):
    bool_array = [False, False] + [True] * n
    for i in range(2, int(ceil(sqrt(n)))):
        if bool_array[i]:
            for j in range(i * i, n + 1, i):
                bool_array[j] = False
    primes = [i for i in range(n + 1) if bool_array[i]]
    return primes
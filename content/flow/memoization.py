# Top-Down DP
# Remember previous computation result, prevent unnecessary computation
import functools
@functools.lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2: return n
    return fibonacci(n - 1) + fibonacci(n - 2)
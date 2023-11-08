# Bottom-up DP
# Fill a table, then compute solution from table
def fibonacci(n):
    m = [0, 1]
    for i in range(2, n+1):
        m.append(m[i-2] + m[i-1])
    return m[n]
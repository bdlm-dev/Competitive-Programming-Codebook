# Returns size of, LIS, of array of numbers
def longest_increasing_subsequence(n):
    c = [1] * len(n)
    loc = [-1] * len(n)
    for i in range(1, len(n)):
        for j in range(0, i):
            if n[i] > n[j]:
                if c[j] + 1 > c[i]:
                    c[i] = c[j] + 1
                    loc[i] = j
    m = max(c)
    sol = []
    i = c.index(m)
    while loc[i] > -1:
        sol.append(n[i])
        i = loc[i]
    sol.append(n[i])
    return m, sol[::-1]
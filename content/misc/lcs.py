# Finds length of longest common subsequence, order maintained
def longest_common_subsequence(s1, s2):
    m, n = len(s1), len(s2)
    c = [[0 for j in range(n + 1)] for i in range(m + 1)]
    for i, c_s1 in enumerate(s1):
        for j, c_s2 in enumerate(s2):
            if c_s1 == c_s2:
                c[i + 1][j + 1] = c[i][j] + 1
            else:
                c[i + 1][j + 1] = max(c[i][j + 1], c[i + 1][j])
    seq = ""
    i, j = m, n
    while i >= 1 and j >= 1:
        if s1[i - 1] == s2[j - 1]:
            seq += s1[i - 1]
            i, j = i - 1, j - 1
        elif c[i - 1][j] > c[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return len(seq), seq[::-1]
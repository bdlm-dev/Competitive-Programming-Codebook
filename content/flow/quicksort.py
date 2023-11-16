def qsort(a, start, end):
    """ quicksort in O(nlogn), no extra memory, in-place"""
    if start < end:
        p = choosepivot(start, end)
        if p != start:
            a[p], a[start] = a[start], a[p]
        equal = partition(a, start, end)
        qsort(a, start, equal-1)
        qsort(a, equal+1, end)
def partition(a, l, r):
    pivot, i = a[l], l+1
    for j in range(l+1, r+1):
        if a[j] <= pivot:
            a[i],a[j] = a[j],a[i]
            i += 1
    # swap pivot to its correct place
    a[l], a[i-1] = a[i-1], a[l]
    return i-1
def choosepivot(s, e):
    return randint(s,e)
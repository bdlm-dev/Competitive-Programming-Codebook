import bisect
# Returns index of x or -1 if not found
def binary_search(arr, x):
    i = bisect.bisect_left(arr, x)
    if i != len(arr) and arr[i] == x:
        return i
    else:
        return -1
# binary search about a continuous interval
# e.g. NWERC 2022 Circular Caramel Cookie
def binary_search_continuous(f, x, lim=1e-9):
    l, r = 0, 1e6
    while r - l > lim:
        mid = l + (r - l) / 2
        if f(mid) > x:
            r = mid
        else:
            l = mid
    return l + (r-l)/2
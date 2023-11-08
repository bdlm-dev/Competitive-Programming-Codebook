import bisect
# Returns index of x or -1 if not found
def binary_search(arr, x):
    i = bisect.bisect_left(arr, x)
    if i != len(arr) and arr[i] == x:
        return i
    else:
        return -1
# Example implementation of heap
# Practically equivalent to minimum-spanning-tree
# Example problem this solves:
# Given N ropes of different lengths, find the minimum cost to connect these ropes, cost is the sum of their lengths
import heapq
def min(arr):
    n = len(arr)
    heapq.heapify(arr) # transform arr into heap in-place
    res = 0
    while(len(arr) > 1):
        first = heapq.heappop(arr)
        second = heapq.heappop(arr)
        res += first + second
        heapq.heappush(arr, first + second)
    return res
smallest_k = heapq.nsmallest(k, heap)
largest_k = heapq.nlargest(k, heap)
# Push to heap, pop & return smallest
smallest = heapq.heappushpop(heap, item)
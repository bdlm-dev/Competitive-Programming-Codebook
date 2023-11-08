class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * (4 * self.n)
        self.nums = nums
        self.build(1, 0, self.n - 1)
    def build(self, node, start, end):
        if start == end:
            self.tree[node] = self.nums[start]
        else:
            mid = (start + end) // 2
            left_node = node * 2
            right_node = node * 2 + 1
            self.build(left_node, start, mid)
            self.build(right_node, mid + 1, end)
            self.tree[node] = self.tree[left_node] + self.tree[right_node]
    def query(self, L, R):
        return self._query(1, 0, self.n - 1, L, R)
    def _query(self, node, start, end, L, R):
        if R < start or L > end:
            return 0
        if L <= start and R >= end:
            return self.tree[node]
        mid = (start + end) // 2
        left_sum = self._query(node * 2, start, mid, L, R)
        right_sum = self._query(node * 2 + 1, mid + 1, end, L, R)
        return left_sum + right_sum
    def update(self, index, value):
        self._update(1, 0, self.n - 1, index, value)
    def _update(self, node, start, end, index, value):
        if start == end:
            self.tree[node] = value
            self.nums[index] = value
        else:
            mid = (start + end) // 2
            if start <= index <= mid:
                self._update(node * 2, start, mid, index, value)
            else:
                self._update(node * 2 + 1, mid + 1, end, index, value)
            self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]


data = [3, 7, 2, 8, 5]
tree = SegmentTree(data)
tree.update(2, 4)  # Update: Set the value at index 1 to 2
print(tree.query(1, 4)) # Query total in range [1, 4] inclusive
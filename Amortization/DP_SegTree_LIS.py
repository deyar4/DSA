class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)  # n is the number of elements in the array
        self.tree = [0] * (4 * self.n)  # Initialize the segment tree with size 4*n
        self.build(nums, 1, 0, self.n - 1)

    def build(self, nums, treeIndex, lo, hi):
        # This function builds the segment tree in a bottom-up manner
        if lo == hi:
            self.tree[treeIndex] = nums[lo]
            return
        mid = (lo + hi) // 2
        self.build(nums, treeIndex * 2, lo, mid)
        self.build(nums, treeIndex * 2 + 1, mid + 1, hi)
        # Each node of the segment tree is visited exactly once during the build process.
        # Hence, the time complexity of build operation is O(n).

    def query(self, treeIndex, lo, hi, left, right):
        # This function is used to perform range queries on the segment tree
        if lo > right or hi < left:
            return 0
        if lo >= left and hi <= right:
            return self.tree[treeIndex]
        mid = (lo + hi) // 2
        return max(self.query(treeIndex * 2, lo, mid, left, right),
                   self.query(treeIndex * 2 + 1, mid + 1, hi, left, right))
        # The query operation has a time complexity of O(log n) since each time it halves the range.

    def update(self, treeIndex, lo, hi, index, value):
        # This function is used to update a value in the segment tree
        if lo == hi:
            self.tree[treeIndex] = value
            return
        mid = (lo + hi) // 2
        if index <= mid:
            self.update(treeIndex * 2, lo, mid, index, value)
        else:
            self.update(treeIndex * 2 + 1, mid + 1, hi, index, value)
        self.tree[treeIndex] = max(self.tree[treeIndex * 2], self.tree[treeIndex * 2 + 1])
        # The update operation also has a time complexity of O(log n) because it traverses the tree to the leaf level.

def longest_increasing_subsequence(nums):
    n = len(nums)
    if n == 0:
        return 0

    dp = [1] * n
    segment_tree = SegmentTree(dp)

    for i in range(1, n):
        max_val = segment_tree.query(1, 0, n - 1, 0, nums[i] - 1)
        dp[i] = max_val + 1
        segment_tree.update(1, 0, n - 1, nums[i], dp[i])
        # In each iteration, both the query and update operations on the segment tree are performed.
        # Both of these operations have a time complexity of O(log n).
        # Since there are n elements in the array, the total time complexity for the loop is O(n log n).

    return max(dp)


nums = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print("Length of Longest Increasing Subsequence:", longest_increasing_subsequence(nums))

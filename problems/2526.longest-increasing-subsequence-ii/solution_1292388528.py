# 2526 - Longest Increasing Subsequence II
# Date: 2024-06-18
# Runtime: 4332 ms, Memory: 29.4 MB
# Submission Id: 1292388528


class SegmentTree:
    def __init__(self, size):
        self.tree = [0] * size * 4
        self.size = size

    def update(self, left, right, idx, pos, val):
        if left > pos or right < pos:
            return
        if left == right:
            self.tree[idx] = val
            return

        mid = (left + right) // 2
        self.update(left, mid, 2*idx+1, pos, val)
        self.update(mid+1, right, 2*idx+2, pos, val)
        self.tree[idx] = max(self.tree[2*idx+1], self.tree[2*idx+2])

    def query(self, left, right, idx, query_s, query_e):
        if query_e < left or query_s > right:
            return 0
        if query_s <= left and query_e >= right:
            return self.tree[idx]

        mid = (left + right) // 2
        return max(
            self.query(left, mid, 2*idx+1, query_s, query_e),
            self.query(mid+1, right, 2*idx+2, query_s, query_e)
        )

class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        size = max(nums) + 1
        segment_tree = SegmentTree(size)
        ans = 0
        for num in nums:
            length = segment_tree.query(0, size-1, 0, num-k, num-1) + 1
            ans = max(ans, length)
            segment_tree.update(0, size-1, 0, num, length)
        return ans
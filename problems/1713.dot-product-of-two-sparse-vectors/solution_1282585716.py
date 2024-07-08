# 1713 - Dot Product of Two Sparse Vectors
# Date: 2024-06-09
# Runtime: 1600 ms, Memory: 20.1 MB
# Submission Id: 1282585716


class SparseVector:
    def __init__(self, nums: List[int]):
        self.table = {}
        for idx, num in enumerate(nums):
            if num:
                self.table[idx] = num

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        for idx, num in self.table.items():
            res += num * vec.table.get(idx, 0)
        return res

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
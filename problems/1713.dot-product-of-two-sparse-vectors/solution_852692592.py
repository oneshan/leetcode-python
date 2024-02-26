# 1713 - Dot Product of Two Sparse Vectors
# Date: 2022-12-01
# Runtime: 2561 ms, Memory: 17.8 MB
# Submission Id: 852692592


class SparseVector:
    def __init__(self, nums: List[int]):
        self.data = {}
        for idx, num in enumerate(nums):
            if num:
                self.data[idx] = num

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        ans = 0
        for idx in self.data:
            if idx in vec.data:
                ans += self.data[idx] * vec.data[idx]
        return ans

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
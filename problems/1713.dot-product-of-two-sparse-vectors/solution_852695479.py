# 1713 - Dot Product of Two Sparse Vectors
# Date: 2022-12-01
# Runtime: 1708 ms, Memory: 18.8 MB
# Submission Id: 852695479


class SparseVector:
    def __init__(self, nums: List[int]):
        self.data = [(idx, num) for idx, num in enumerate(nums) if num]
        self.size = len(self.data)

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        ans = p1 = p2 = 0
        while p1 < self.size and p2 < vec.size:
            if self.data[p1][0] == vec.data[p2][0]:
                ans += self.data[p1][1] * vec.data[p2][1]
                p1 += 1
                p2 += 1
            elif self.data[p1][0] < vec.data[p2][0]:
                p1 += 1
            else:
                p2 += 1
        return ans

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
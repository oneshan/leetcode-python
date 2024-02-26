# 1713 - Dot Product of Two Sparse Vectors
# Date: 2022-12-01
# Runtime: 4618 ms, Memory: 18.9 MB
# Submission Id: 852699386


class SparseVector:
    def __init__(self, nums: List[int]):
        self.data = [(idx, num) for idx, num in enumerate(nums) if num]
        self.size = len(self.data)

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        ans = 0
        p2 = 0
        for pair in self.data:
            p2 = self.binary_search(vec, p2, vec.size-1, pair[0])
            if p2 == vec.size:
                break
            if pair[0] == vec.data[p2][0]:
                ans += pair[1] * vec.data[p2][1]
        return ans
    
    def binary_search(self, vec, left, right, target):
        while left <= right:
            mid = (left + right) // 2
            if vec.data[mid][0] == target:
                return mid
            if vec.data[mid][0] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
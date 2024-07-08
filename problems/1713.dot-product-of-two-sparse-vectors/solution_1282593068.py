# 1713 - Dot Product of Two Sparse Vectors
# Date: 2024-06-09
# Runtime: 2360 ms, Memory: 36.9 MB
# Submission Id: 1282593068


class SparseVector:
    def __init__(self, nums: List[int]):
        self.data = [(idx, num) for idx, num in enumerate(nums) if nums]
        self.size = len(self.data)

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        for idx, num in self.data:
            p2 = self.binary_search(vec.data, idx)
            if p2 == vec.size:
                break
            if vec.data[p2][0] == idx:
                res += vec.data[p2][1] * num
        return res

    def binary_search(self, arr, target):
        left, right = 0, len(arr)-1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid][0] == target:
                return mid
            if arr[mid][0] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
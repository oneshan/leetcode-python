# 0189 - Rotate Array
# Date: 2022-12-19
# Runtime: 246 ms, Memory: 25.5 MB
# Submission Id: 862012299


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        self.reverse(nums, 0, n-k-1)
        self.reverse(nums, n-k, n-1)
        self.reverse(nums, 0, n-1)
    
    def reverse(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left, right = left + 1, right - 1
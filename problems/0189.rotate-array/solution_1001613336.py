# 0189 - Rotate Array
# Date: 2023-07-23
# Runtime: 236 ms, Memory: 28 MB
# Submission Id: 1001613336


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        n = len(nums)
        k %= n
        
        reverse(0, n-1)
        reverse(0, k-1)
        reverse(k, n-1)

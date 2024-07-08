# 0031 - Next Permutation
# Date: 2024-06-07
# Runtime: 41 ms, Memory: 16.6 MB
# Submission Id: 1279709064


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        # find first decreasing
        i = n-2
        while i >= 0 and nums[i+1] <= nums[i]:
            i -= 1
        
        # find first num larger than nums[i] and swap
        if i >= 0:
            j = n-1
            while nums[j] <= nums[i]:
                j -= 1                
            nums[i], nums[j] = nums[j], nums[i]

        # reverse nums[i+1:]
        left, right = i+1, n-1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
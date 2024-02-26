# 0031 - Next Permutation
# Date: 2022-12-06
# Runtime: 102 ms, Memory: 13.8 MB
# Submission Id: 855544169


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        j = n-1
        while j and nums[j] <= nums[j-1]:
            j -= 1
        
        if j > 0:
            i = n-1
            while i and nums[i] <= nums[j-1]:
                i -= 1
            nums[i], nums[j-1] = nums[j-1], nums[i]
        
        left, right = j, n-1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
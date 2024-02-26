# 0283 - Move Zeroes
# Date: 2023-08-17
# Runtime: 132 ms, Memory: 17.9 MB
# Submission Id: 1023776517


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for num in nums:
            if num:
                nums[i] = num
                i += 1
        
        for j in range(i, len(nums)):
            nums[j] = 0
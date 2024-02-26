# 0283 - Move Zeroes
# Date: 2022-09-16
# Runtime: 345 ms, Memory: 15.5 MB
# Submission Id: 801349110


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = 0
        for num in nums:
            if num:
                nums[idx] = num
                idx += 1
        while idx < len(nums):
            nums[idx] = 0
            idx += 1
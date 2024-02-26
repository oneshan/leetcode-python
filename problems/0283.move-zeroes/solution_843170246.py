# 0283 - Move Zeroes
# Date: 2022-11-14
# Runtime: 169 ms, Memory: 15.5 MB
# Submission Id: 843170246


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_idx = 0
        for curr in range(len(nums)):
            if nums[curr] != 0:
                nums[zero_idx], nums[curr] = nums[curr], nums[zero_idx]
                zero_idx += 1
# 0283 - Move Zeroes
# Date: 2022-07-13
# Runtime: 314 ms, Memory: 15.7 MB
# Submission Id: 746090634


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
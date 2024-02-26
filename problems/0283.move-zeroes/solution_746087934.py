# 0283 - Move Zeroes
# Date: 2022-07-13
# Runtime: 241 ms, Memory: 15.7 MB
# Submission Id: 746087934


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = 0
        for num in nums:
            if num != 0:
                nums[idx] = num
                idx += 1
        for tmp in range(idx, len(nums)):
            nums[tmp] = 0
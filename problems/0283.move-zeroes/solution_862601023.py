# 0283 - Move Zeroes
# Date: 2022-12-20
# Runtime: 175 ms, Memory: 15.5 MB
# Submission Id: 862601023


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        for num in nums:
            if num:
                nums[left] = num
                left += 1
        for i in range(left, len(nums)):
            nums[i] = 0
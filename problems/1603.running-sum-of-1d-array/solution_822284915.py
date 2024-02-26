# 1603 - Running Sum of 1d Array
# Date: 2022-10-14
# Runtime: 56 ms, Memory: 14.1 MB
# Submission Id: 822284915


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums
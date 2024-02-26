# 1603 - Running Sum of 1d Array
# Date: 2023-08-15
# Runtime: 54 ms, Memory: 16.5 MB
# Submission Id: 1022149265


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums
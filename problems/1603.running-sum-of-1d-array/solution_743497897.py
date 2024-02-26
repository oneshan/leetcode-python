# 1603 - Running Sum of 1d Array
# Date: 2022-07-10
# Runtime: 46 ms, Memory: 14 MB
# Submission Id: 743497897


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for idx in range(1, len(nums)):
            nums[idx] += nums[idx-1]
        return nums
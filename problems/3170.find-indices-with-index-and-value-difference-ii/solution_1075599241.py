# 3170 - Find Indices With Index and Value Difference II
# Date: 2023-10-15
# Runtime: 619 ms, Memory: 30.2 MB
# Submission Id: 1075599241


class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        n = len(nums)
        curr_min = curr_max = 0
        for i in range(indexDifference, n):
            if nums[i-indexDifference] < nums[curr_min]:
                curr_min = i - indexDifference
            if nums[i-indexDifference] > nums[curr_max]:
                curr_max = i - indexDifference
            if nums[i] - nums[curr_min] >= valueDifference:
                return [curr_min, i]
            if nums[curr_max] - nums[i] >= valueDifference:
                return [curr_max, i]
        return [-1, -1]
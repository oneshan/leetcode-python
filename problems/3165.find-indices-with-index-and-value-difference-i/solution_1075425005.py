# 3165 - Find Indices With Index and Value Difference I
# Date: 2023-10-15
# Runtime: 59 ms, Memory: 16.3 MB
# Submission Id: 1075425005


class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i+indexDifference, n):
                if abs(nums[i] - nums[j]) >= valueDifference:
                    return [i, j]
        return [-1, -1]
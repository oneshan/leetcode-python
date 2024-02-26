# 2042 - Maximum Product Difference Between Two Pairs
# Date: 2023-12-18
# Runtime: 159 ms, Memory: 17.7 MB
# Submission Id: 1122267605


class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        return (nums[0] * nums[1]) - (nums[-2] * nums[-1])
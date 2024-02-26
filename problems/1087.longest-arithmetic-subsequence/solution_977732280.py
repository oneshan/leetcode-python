# 1087 - Longest Arithmetic Subsequence
# Date: 2023-06-23
# Runtime: 2901 ms, Memory: 60.6 MB
# Submission Id: 977732280


class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = {}
        for right in range(len(nums)):
            for left in range(right):
                diff = nums[right] - nums[left]
                dp[(right, diff)] = dp.get((left, diff), 1) + 1
        return max(dp.values())
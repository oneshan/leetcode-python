# 1896 - Maximum Score from Performing Multiplication Operations
# Date: 2024-04-11
# Runtime: 1016 ms, Memory: 152.1 MB
# Submission Id: 1229224161


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n = len(nums)

        @cache
        def dp(left, i):
            if i == len(multipliers):
                return 0
            return max(
                nums[left] * multipliers[i] + dp(left+1, i+1),
                nums[n-1-i+left] * multipliers[i] + dp(left, i+1)
            )

        return dp(0, 0)
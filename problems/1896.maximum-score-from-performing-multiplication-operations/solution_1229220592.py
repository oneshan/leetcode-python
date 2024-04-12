# 1896 - Maximum Score from Performing Multiplication Operations
# Date: 2024-04-11
# Runtime: 1013 ms, Memory: 177.8 MB
# Submission Id: 1229220592


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        
        @cache
        def dp(left, right, i):
            if i == len(multipliers):
                return 0
            return max(
                nums[left] * multipliers[i] + dp(left+1, right, i+1),
                nums[right] * multipliers[i] + dp(left, right-1, i+1)
            )

        return dp(0, len(nums)-1, 0)
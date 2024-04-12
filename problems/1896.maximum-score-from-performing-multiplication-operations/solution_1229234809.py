# 1896 - Maximum Score from Performing Multiplication Operations
# Date: 2024-04-11
# Runtime: 787 ms, Memory: 27.9 MB
# Submission Id: 1229234809


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        m = len(multipliers)
        n = len(nums)

        prev = [0] * (n+1)
        for i in range(m-1, -1, -1):
            dp = [0] * (n+1)
            for left in range(i+1):
                right = (n-1) - (i-left)
                dp[left] = max(
                    prev[left+1] + nums[left] * multipliers[i],
                    prev[left] + nums[right] * multipliers[i],
                )
            prev = dp

        return dp[0]
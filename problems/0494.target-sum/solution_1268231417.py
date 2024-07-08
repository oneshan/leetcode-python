# 0494 - Target Sum
# Date: 2024-05-26
# Runtime: 188 ms, Memory: 16.5 MB
# Submission Id: 1268231417


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        dp = [0] * 2001
        dp[1000] = 1

        for num in nums:
            next_dp = [0] * 2001
            for i in range(2001):
                if dp[i] > 0:
                    if i - num >= 0:
                        next_dp[i-num] += dp[i]
                    if i + num < 2001:
                        next_dp[i+num] += dp[i]
            dp = next_dp

        return dp[1000+target]
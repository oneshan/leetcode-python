# 0494 - Target Sum
# Date: 2024-05-26
# Runtime: 233 ms, Memory: 16.5 MB
# Submission Id: 1268224943


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        dp = Counter()
        dp[0] = 1

        for num in nums:
            next_dp = Counter()
            for i in dp:
                next_dp[i+num] += dp[i]
                next_dp[i-num] += dp[i]
            dp = next_dp
        return dp[target]
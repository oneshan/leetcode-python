# 0312 - Burst Balloons
# Date: 2024-05-27
# Runtime: 2956 ms, Memory: 18.5 MB
# Submission Id: 1269395568


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)

        dp = [[0] * n for _ in range(n)]

        for left in range(n-2, 0, -1):
            for right in range(left, n-1):
                for i in range(left, right + 1):
                    coins = nums[left-1] * nums[i] * nums[right+1]
                    remains = dp[left][i-1] + dp[i+1][right]
                    dp[left][right] = max(dp[left][right], coins + remains)
        return dp[1][-2]
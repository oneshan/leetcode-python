# 1393 - Maximum Value of K Coins From Piles
# Date: 2023-04-15
# Runtime: 7877 ms, Memory: 38.5 MB
# Submission Id: 933995736


class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)
        dp = [[0] * (k+1) for _ in range(n+1)]
        for i in range(n):
            for coins in range(k+1):
                dp[i+1][coins] = dp[i][coins]
                curr_sum = 0
                for curr_coins in range(1, min(len(piles[i]), coins) + 1):
                    curr_sum += piles[i][curr_coins-1]
                    dp[i+1][coins] = max(dp[i+1][coins],
                                         dp[i][coins-curr_coins] + curr_sum)
        return dp[-1][k]
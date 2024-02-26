# 1393 - Maximum Value of K Coins From Piles
# Date: 2023-04-15
# Runtime: 4969 ms, Memory: 14.3 MB
# Submission Id: 934001439


class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        dp = [0] * (k+1)
        prefix_sum = [0] * (k+1)
            
        for pile in piles:
            
            prefix_sum[0] = 0  # reset
            for i in range(min(len(pile), k)):
                prefix_sum[i+1] = prefix_sum[i] + pile[i]
            
            for i in range(k, 0, -1):
                curr_max = 0
                for j in range(min(len(pile), i), -1, -1):
                    curr_max = max(curr_max, prefix_sum[j] + dp[i-j])
                dp[i] = curr_max

        return dp[-1]
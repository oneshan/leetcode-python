# 1393 - Maximum Value of K Coins From Piles
# Date: 2023-04-15
# Runtime: 4966 ms, Memory: 14.4 MB
# Submission Id: 934000898


class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        dp = [0] * (k+1)
        
        for pile in piles:
            curr_sum = 0
            
            prefix_sum = [0] * (k+1)
            for i in range(min(len(pile), k)):
                prefix_sum[i+1] = prefix_sum[i] + pile[i]
            
            for i in range(k, 0, -1):
                curr_max = 0
                for j in range(min(len(pile), i), -1, -1):
                    curr_max = max(curr_max, prefix_sum[j] + dp[i-j])
                dp[i] = curr_max

        return dp[-1]
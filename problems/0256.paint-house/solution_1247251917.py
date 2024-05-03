# 0256 - Paint House
# Date: 2024-05-02
# Runtime: 53 ms, Memory: 16.4 MB
# Submission Id: 1247251917


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        dp = costs[0]
        for i in range(1, len(costs)):
            dp = [
                min(dp[1], dp[2]) + costs[i][0],
                min(dp[0], dp[2]) + costs[i][1],
                min(dp[0], dp[1]) + costs[i][2],
            ]
            
        return min(dp)
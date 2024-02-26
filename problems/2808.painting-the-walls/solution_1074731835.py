# 2808 - Painting the Walls
# Date: 2023-10-14
# Runtime: 1208 ms, Memory: 19.5 MB
# Submission Id: 1074731835


class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        
        dp = [[0] * (n+1) for _ in range(n+1)]
        for i in range(1, n+1):
            dp[n][i] = inf
        
        for i in range(n-1, -1, -1):
            for remain in range(1, n+1):
                dp[i][remain] = min(dp[i+1][remain], dp[i+1][max(0, remain-1-time[i])] + cost[i])
        
        return dp[0][n]
# 2808 - Painting the Walls
# Date: 2023-10-14
# Runtime: 1031 ms, Memory: 16.4 MB
# Submission Id: 1074732854


class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        
        prev_dp = [inf] * (n+1)
        prev_dp[0] = 0
        
        for i in range(n):
            dp = [0] * (n+1)
            for remain in range(1, n+1):
                dp[remain] = min(prev_dp[remain], prev_dp[max(0, remain-1-time[i])] + cost[i])
            prev_dp = dp
        
        return dp[n]
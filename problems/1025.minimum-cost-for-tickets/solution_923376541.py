# 1025 - Minimum Cost For Tickets
# Date: 2023-03-28
# Runtime: 50 ms, Memory: 13.9 MB
# Submission Id: 923376541


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * (days[-1]+1)
        days = set(days)
        
        for i in range(1, len(dp)):
            if i in days:
                dp[i] = min(dp[max(i-1,0)]+costs[0],
                            dp[max(i-7,0)]+costs[1],
                            dp[max(i-30,0)]+costs[2])
            else:
                dp[i] = dp[i-1]
        return dp[-1]
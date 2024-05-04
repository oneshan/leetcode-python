# 1025 - Minimum Cost For Tickets
# Date: 2024-05-03
# Runtime: 44 ms, Memory: 16.6 MB
# Submission Id: 1248093285


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        days = set(days)

        dp = [0] * 366
        for d in range(1, 366):
            if d in days:
                dp[d] = min(
                    costs[0] + dp[d-1],
                    costs[1] + dp[d-7],
                    costs[2] + dp[d-30],
                )
            else:
                dp[d] = dp[d-1]
        
        return dp[-1]
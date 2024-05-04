# 1025 - Minimum Cost For Tickets
# Date: 2024-05-03
# Runtime: 48 ms, Memory: 19.2 MB
# Submission Id: 1248089257


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        @cache
        def dp(i, pass_day):
            if i == len(days):
                return 0
            if days[i] < pass_day:
                return dp(i+1, pass_day)
            return min(
                costs[0] + dp(i+1, days[i] + 1),
                costs[1] + dp(i+1, days[i] + 7),
                costs[2] + dp(i+1, days[i] + 30),
            )
        
        return dp(0, 0)
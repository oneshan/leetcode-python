# 1025 - Minimum Cost For Tickets
# Date: 2023-03-28
# Runtime: 51 ms, Memory: 15.8 MB
# Submission Id: 923378296


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dayset = set(days)
        cache = {}

        def dp(i):
            if i > 365:
                return 0
            if i not in cache:
                if i in dayset:
                    cache[i] = min(dp(i+1) + costs[0],
                                   dp(i+7) + costs[1],
                                   dp(i+30) + costs[2])
                else:
                    cache[i] = dp(i+1)
            return cache[i]
        
        return dp(1)
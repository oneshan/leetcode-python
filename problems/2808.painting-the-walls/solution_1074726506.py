# 2808 - Painting the Walls
# Date: 2023-10-14
# Runtime: 1991 ms, Memory: 469.1 MB
# Submission Id: 1074726506


class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        
        @cache
        def dp(i, remain):
            if remain <= 0:
                return 0
            if i == n:
                return inf
            
            a = dp(i+1, remain)
            b = dp(i+1, remain-1-time[i]) + cost[i]
            return min(a, b)
        
        return dp(0, n)
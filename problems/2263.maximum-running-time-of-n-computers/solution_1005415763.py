# 2263 - Maximum Running Time of N Computers
# Date: 2023-07-27
# Runtime: 493 ms, Memory: 31 MB
# Submission Id: 1005415763


class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort()
        
        extra = sum(batteries[:-n])
        live = batteries[-n:]
        for i in range(1, n):
            minus = (live[i] - live[i-1]) * i
            if extra < minus:
                return live[i-1] + extra // i
            extra -= minus
        return live[-1] + extra // n            
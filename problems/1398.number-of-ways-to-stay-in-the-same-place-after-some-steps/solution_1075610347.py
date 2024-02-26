# 1398 - Number of Ways to Stay in the Same Place After Some Steps
# Date: 2023-10-15
# Runtime: 413 ms, Memory: 108.5 MB
# Submission Id: 1075610347


class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 1_000_000_007
        
        @cache
        def dp(curr, remain):
            if remain == 0:
                return 1 if curr == 0 else 0
            
            count = dp(curr, remain-1)
            if curr > 0:
                count = (count + dp(curr-1, remain-1)) % MOD
            
            if curr < arrLen-1:
                count = (count + dp(curr+1, remain-1)) % MOD
            return count
        
        return dp(0, steps)
# 1398 - Number of Ways to Stay in the Same Place After Some Steps
# Date: 2023-10-15
# Runtime: 336 ms, Memory: 22.1 MB
# Submission Id: 1075613497


class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 1_000_000_007
        
        arrLen = min(arrLen, steps)
        dp = [[0] * (steps+1) for _ in range(arrLen)]
        dp[0][0] = 1
        
        for remain in range(1, steps+1):
            for curr in range(arrLen-1, -1, -1):
                count = dp[curr][remain-1]
                if curr > 0:
                    count = (count + dp[curr-1][remain-1]) % MOD
                if curr < arrLen-1:
                    count = (count + dp[curr+1][remain-1]) % MOD
                dp[curr][remain] = count
                
        return dp[0][-1]
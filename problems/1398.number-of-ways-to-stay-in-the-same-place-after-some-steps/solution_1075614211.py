# 1398 - Number of Ways to Stay in the Same Place After Some Steps
# Date: 2023-10-15
# Runtime: 260 ms, Memory: 16.2 MB
# Submission Id: 1075614211


class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 1_000_000_007
        
        arrLen = min(arrLen, steps)
        prev_dp = [0] * (steps+1)
        prev_dp[0] = 1
        
        for remain in range(1, steps+1):
            dp = [0] * (steps+1)
            for curr in range(arrLen-1, -1, -1):
                count = prev_dp[curr]
                if curr > 0:
                    count = (count + prev_dp[curr-1]) % MOD
                if curr < arrLen-1:
                    count = (count + prev_dp[curr+1]) % MOD
                dp[curr] = count
            prev_dp = dp
                
        return prev_dp[0]
# 1263 - Number of Dice Rolls With Target Sum
# Date: 2024-05-03
# Runtime: 292 ms, Memory: 16.7 MB
# Submission Id: 1248100858


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 1_000_000_007
        
        dp = [0] * (target+1)
        dp[0] = 1
        for _ in range(n):
            new_dp = [0] * (target+1)
            for _sum in range(target+1):
                res = 0
                for i in range(1, k+1):
                    if _sum - i < 0:
                        break
                    res += dp[_sum - i]
                new_dp[_sum] = res % MOD
            dp = new_dp
        return dp[-1]        
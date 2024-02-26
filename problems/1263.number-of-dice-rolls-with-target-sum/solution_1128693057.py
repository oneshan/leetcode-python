# 1263 - Number of Dice Rolls With Target Sum
# Date: 2023-12-26
# Runtime: 400 ms, Memory: 17.9 MB
# Submission Id: 1128693057


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 1_000_000_007
        
        dp = [[0] * (target+1) for _ in range(n+1)]
        dp[n][target] = 1
        
        for _dice in range(n-1, -1, -1):
            for _sum in range(0, target+1):
                res = 0
                for i in range(1, k+1):
                    if _sum+i > target:
                        break
                    res = (res + dp[_dice+1][_sum+i]) % MOD
                dp[_dice][_sum] = res
        
        return dp[0][0]
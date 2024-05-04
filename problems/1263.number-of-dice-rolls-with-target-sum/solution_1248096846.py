# 1263 - Number of Dice Rolls With Target Sum
# Date: 2024-05-03
# Runtime: 217 ms, Memory: 22.1 MB
# Submission Id: 1248096846


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 1_000_000_007
        
        @cache
        def dp(i, total):
            if i == n and total == target:
                return 1
            if i > n or total > target:
                return 0
            
            res = 0
            for j in range(1, k+1):
                res += dp(i + 1, total + j)
            return res % MOD
        
        return dp(0, 0)
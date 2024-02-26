# 1263 - Number of Dice Rolls With Target Sum
# Date: 2023-12-26
# Runtime: 239 ms, Memory: 23.5 MB
# Submission Id: 1128689467


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 1_000_000_007
        
        @cache
        def dfs(count, total):
            if count == 0 and total == 0:
                return 1
            if count < 0 or total < 0:
                return 0
            
            res = 0
            for i in range(1, k+1):
                res += dfs(count-1, total-i)
            return res % MOD
        
        return dfs(n, target)
# 1263 - Number of Dice Rolls With Target Sum
# Date: 2023-12-26
# Runtime: 394 ms, Memory: 17.3 MB
# Submission Id: 1128693962


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 1_000_000_007
        
        dp = [0] * (target+1)
        dp[target] = 1
        
        for _ in range(n):
            new_dp = [0] * (target+1)
            for _sum in range(0, target+1):
                res = 0
                for i in range(1, k+1):
                    if _sum+i > target:
                        break
                    res = (res + dp[_sum+i]) % MOD
                new_dp[_sum] = res
            dp = new_dp
        
        return dp[0]
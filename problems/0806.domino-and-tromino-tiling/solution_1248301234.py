# 0806 - Domino and Tromino Tiling
# Date: 2024-05-03
# Runtime: 49 ms, Memory: 19.6 MB
# Submission Id: 1248301234


class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 1_000_000_007
        
        @cache
        def dp(r1, r2):
            if r1 == n and r2 == n:
                return 1
            if r1 > n or r2 > n:
                return 0

            res = 0
            # domino tile
            if r1 == r2:
                res += dp(r1+1, r2+1)
                res += dp(r1+2, r2+2)
            elif r1 > r2:
                res += dp(r1, r2+2)
            else:
                res += dp(r1+2, r2)
            
            # tromino tile
            if r1 >= r2:
                res += dp(r1+1, r2+2)
            if r1 <= r2:
                res += dp(r1+2, r2+1)

            return res % MOD
        
        return dp(0, 0)
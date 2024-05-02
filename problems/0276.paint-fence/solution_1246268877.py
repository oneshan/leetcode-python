# 0276 - Paint Fence
# Date: 2024-05-01
# Runtime: 44 ms, Memory: 16.6 MB
# Submission Id: 1246268877


class Solution:
    def numWays(self, n: int, k: int) -> int:
        
        @cache
        def dp(i):
            if i == 1:
                return k
            if i == 2:
                return k * k
            # diff color
            res = (k-1) * dp(i-1)
            # same color
            res += 1 * (k-1) * dp(i-2)

            return res
        
        return dp(n)
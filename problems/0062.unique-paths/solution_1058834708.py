# 0062 - Unique Paths
# Date: 2023-09-25
# Runtime: 33 ms, Memory: 16.6 MB
# Submission Id: 1058834708


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        @cache
        def dp(r, c):
            if r < 0 or c < 0:
                return 0
            if r == c == 0:
                return 1
            
            return dp(r-1, c) + dp(r, c-1)
        
        return dp(m-1, n-1)
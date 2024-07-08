# 0650 - 2 Keys Keyboard
# Date: 2024-06-11
# Runtime: 134 ms, Memory: 34.8 MB
# Submission Id: 1284674572


class Solution:
    def minSteps(self, n: int) -> int:
        
        @cache
        def dp(chars, clipboard):
            if chars == n:
                return 0
            if chars > n:
                return float('inf')
            
            # copy
            res = 2 + dp(chars*2, chars)
            # paste
            if clipboard:
                res = min(res, 1 + dp(chars+clipboard, clipboard))
            return res

        return dp(1, 0)
# 0115 - Distinct Subsequences
# Date: 2024-05-27
# Runtime: 40 ms, Memory: 21.1 MB
# Submission Id: 1269174795


class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        @cache
        def dp(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if len(s) - i < len(t) - j:
                return 0
            
            # skip
            res = dp(i+1, j)
            # take
            if s[i] == t[j]:
                res += dp(i+1, j+1)
            return res

        return dp(0, 0)
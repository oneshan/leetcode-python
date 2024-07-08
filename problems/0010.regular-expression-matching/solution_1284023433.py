# 0010 - Regular Expression Matching
# Date: 2024-06-11
# Runtime: 35 ms, Memory: 16.9 MB
# Submission Id: 1284023433


class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        @cache
        def dp(si, pi):
            if pi == len(p):
                return si == len(s)
            
            match = si < len(s) and p[pi] in {s[si], '.'}
            if pi+1 < len(p) and p[pi+1] == '*':
                return dp(si, pi+2) or (match and dp(si+1, pi))
            if match:
                return dp(si+1, pi+1)
                
            return False

        return dp(0, 0)
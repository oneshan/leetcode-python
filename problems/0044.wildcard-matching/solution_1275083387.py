# 0044 - Wildcard Matching
# Date: 2024-06-02
# Runtime: 550 ms, Memory: 152.9 MB
# Submission Id: 1275083387


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        @cache
        def recur(si, pi):
            if pi == len(p):
                return si == len(s)

            if si < len(s) and p[pi] in {s[si], '?'}:
                return recur(si+1, pi+1)

            if p[pi] == '*':
                res = recur(si, pi+1) or recur(si+1, pi+1)
                if si < len(s):
                    res |= recur(si+1, pi)
                return res
            
            return False

        return recur(0, 0)
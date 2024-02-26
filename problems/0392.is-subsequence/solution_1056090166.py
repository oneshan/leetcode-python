# 0392 - Is Subsequence
# Date: 2023-09-22
# Runtime: 36 ms, Memory: 16.2 MB
# Submission Id: 1056090166


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        if not s:
            return True
        n = len(s)
        idx = 0
        for ch in t:
            if s[idx] == ch:
                idx += 1
                if idx == n:
                    return True
        return False
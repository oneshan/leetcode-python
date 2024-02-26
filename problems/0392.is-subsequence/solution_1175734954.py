# 0392 - Is Subsequence
# Date: 2024-02-15
# Runtime: 41 ms, Memory: 16.6 MB
# Submission Id: 1175734954


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
            
        i, n = 0, len(s)
        for ch in t:
            if ch == s[i]:
                i += 1
                if i == n:
                    return True
        return False
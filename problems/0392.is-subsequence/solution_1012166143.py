# 0392 - Is Subsequence
# Date: 2023-08-04
# Runtime: 38 ms, Memory: 16.4 MB
# Submission Id: 1012166143


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        
        s_len, t_len = len(s), len(t)
        if s_len > t_len:
            return False
        
        i = 0
        for ch in t:
            if s[i] == ch:
                i += 1
                if i == s_len:
                    return True
        return False
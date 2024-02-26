# 0392 - Is Subsequence
# Date: 2023-08-04
# Runtime: 45 ms, Memory: 26.8 MB
# Submission Id: 1012170575


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        len_s, len_t = len(s), len(t)
        
        def recur(idx_s, idx_t):
            if idx_s == len_s:
                return True
            if idx_t == len_t:
                return False            
            return recur(idx_s + (s[idx_s] == t[idx_t]), idx_t + 1)
        
        return recur(0, 0)
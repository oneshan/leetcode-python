# 0392 - Is Subsequence
# Date: 2022-11-09
# Runtime: 56 ms, Memory: 13.8 MB
# Submission Id: 839896978


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if len(s) > len(t):
            return False
        
        ptr_s = 0
        for ch in t:
            if s[ptr_s] == ch:
                ptr_s += 1
                if ptr_s == len(s):
                    return True
        return False
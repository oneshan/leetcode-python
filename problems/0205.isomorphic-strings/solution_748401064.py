# 0205 - Isomorphic Strings
# Date: 2022-07-16
# Runtime: 42 ms, Memory: 14.3 MB
# Submission Id: 748401064


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s2t, t2s = {}, {}
        for char_s, char_t in zip(s,t):
            if char_s in s2t and s2t[char_s] != char_t:
                return False
            if char_t in t2s and t2s[char_t] != char_s:
                return False
            s2t[char_s] = char_t
            t2s[char_t] = char_s
        return True
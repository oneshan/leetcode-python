# 0205 - Isomorphic Strings
# Date: 2023-08-30
# Runtime: 44 ms, Memory: 16.5 MB
# Submission Id: 1036083765


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s2t, t2s = {}, {}
        for cs, ct in zip(s, t):
            if s2t.get(cs, ct) != ct:
                return False
            if t2s.get(ct, cs) != cs:
                return False
            s2t[cs] = ct
            t2s[ct] = cs
        return True
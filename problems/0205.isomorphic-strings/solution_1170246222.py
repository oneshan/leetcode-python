# 0205 - Isomorphic Strings
# Date: 2024-02-09
# Runtime: 47 ms, Memory: 16.7 MB
# Submission Id: 1170246222


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s2t, t2s = {}, {}
        for ch_s, ch_t in zip(s, t):
            if ch_s in s2t and s2t[ch_s] != ch_t:
                return False
            if ch_t in t2s and t2s[ch_t] != ch_s:
                return False
            s2t[ch_s] = ch_t
            t2s[ch_t] = ch_s
        return True
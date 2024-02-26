# 0205 - Isomorphic Strings
# Date: 2022-07-11
# Runtime: 51 ms, Memory: 14.1 MB
# Submission Id: 744091903


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        seen_1 = {}
        seen_2 = {}
        for ch_s, ch_t in zip(s, t):
            if ch_s in seen_1 and seen_1[ch_s] != ch_t:
                return False
            if ch_t in seen_2 and seen_2[ch_t] != ch_s:
                return False
            seen_1[ch_s] = ch_t
            seen_2[ch_t] = ch_s
        return True
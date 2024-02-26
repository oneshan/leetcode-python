# 0290 - Word Pattern
# Date: 2022-07-11
# Runtime: 42 ms, Memory: 13.9 MB
# Submission Id: 744111413


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        tokens = s.split()
        if len(pattern) != len(tokens):
            return False
        
        p2t, t2p = {}, {}
        for ch, token in zip(pattern, tokens):
            if ch in p2t and p2t[ch] != token:
                return False
            if token in t2p and t2p[token] != ch:
                return False
            p2t[ch] = token
            t2p[token] = ch
        return True
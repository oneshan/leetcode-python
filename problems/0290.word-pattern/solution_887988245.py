# 0290 - Word Pattern
# Date: 2023-01-30
# Runtime: 17 ms, Memory: 13.9 MB
# Submission Id: 887988245


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        tokens = s.split()
        if len(tokens) != len(pattern):
            return False
        
        c2t, t2c = {}, {}
        
        for ch, token in zip(pattern, tokens):
            if ch not in c2t:
                c2t[ch] = token
            if token not in t2c:
                t2c[token] = ch
            if c2t[ch] != token or t2c[token] != ch:
                return False
        return True
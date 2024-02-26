# 0290 - Word Pattern
# Date: 2023-08-31
# Runtime: 43 ms, Memory: 16.3 MB
# Submission Id: 1036088794


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        tokens = s.split()
        if len(pattern) != len(tokens):
            return False
        
        token_2_pattern = {}
        pattern_2_token = {}
        
        for t, p in zip(pattern, tokens):
            if token_2_pattern.get(t, p) != p:
                return False
            if pattern_2_token.get(p, t) != t:
                return False
            token_2_pattern[t] = p
            pattern_2_token[p] = t
        return True
# 0290 - Word Pattern
# Date: 2023-08-31
# Runtime: 36 ms, Memory: 16.1 MB
# Submission Id: 1036091525


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        tokens = s.split()
        if len(pattern) != len(tokens):
            return False
        
        mapping = {}
        
        for idx, (t, p) in enumerate(zip(pattern, tokens)):
            t_key = f'token_{t}'
            p_key = f'pattern_{p}'
            if mapping.get(t_key) != mapping.get(p_key):
                return False
            mapping[t_key] = mapping[p_key] = idx
        return True
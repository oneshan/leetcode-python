# 0087 - Scramble String
# Date: 2023-03-30
# Runtime: 64 ms, Memory: 14.8 MB
# Submission Id: 924832221


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        
        @cache
        def dfs(s1, s2):
            if s1 == s2:
                return True
            if Counter(s1) != Counter(s2):
                return False
            n = len(s1)
            for k in range(1, n):
                if ((dfs(s1[:k], s2[:k]) and dfs(s1[k:], s2[k:]))
                        or (dfs(s1[:k], s2[n-k:]) and dfs(s1[k:], s2[:n-k]))):
                    return True
            return False
        
        return dfs(s1, s2)
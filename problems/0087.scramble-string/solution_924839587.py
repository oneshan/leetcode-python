# 0087 - Scramble String
# Date: 2023-03-30
# Runtime: 86 ms, Memory: 14.7 MB
# Submission Id: 924839587


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        memo = {}
    
        def dfs(s1, s2):
            if (s1, s2) not in memo:
                if Counter(s1) != Counter(s2):
                    memo[(s1, s2)] = False
                elif s1 == s2:
                    memo[(s1, s2)] = True
                else:
                    n = len(s1)
                    for k in range(1, n):
                        if dfs(s1[:k], s2[:k]) and dfs(s1[k:], s2[k:]):
                            memo[(s1, s2)] = True
                            break
                        if dfs(s1[:k], s2[n-k:]) and dfs(s1[k:], s2[:n-k]):
                            memo[(s1, s2)] = True
                            break
                    else:
                        memo[(s1, s2)] = False
            return memo[(s1, s2)]
        
        return dfs(s1, s2)
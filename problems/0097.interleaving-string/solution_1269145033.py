# 0097 - Interleaving String
# Date: 2024-05-27
# Runtime: 38 ms, Memory: 18.1 MB
# Submission Id: 1269145033


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        @cache
        def dp(i, j):
            if i == len(s1):
                return s2[j:] == s3[i+j:]
            if j == len(s2):
                return s1[i:] == s3[i+j:]
            
            res = False
            if s1[i] == s3[i+j]:
                res |= dp(i+1, j)
            if s2[j] == s3[i+j]:
                res |= dp(i, j+1)
            return res

        return dp(0, 0)
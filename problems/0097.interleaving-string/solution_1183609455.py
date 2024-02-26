# 0097 - Interleaving String
# Date: 2024-02-23
# Runtime: 38 ms, Memory: 17.4 MB
# Submission Id: 1183609455


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        @cache
        def recur(p1, p2, p3):
            if p1 == len(s1):
                return s2[p2:] == s3[p3:]
            if p2 == len(s2):
                return s1[p1:] == s3[p3:]
            if s1[p1] == s3[p3] and recur(p1+1, p2, p3+1):
                return True
            if s2[p2] == s3[p3] and recur(p1, p2+1, p3+1):
                return True
            return False

        return recur(0, 0, 0)
# 0097 - Interleaving String
# Date: 2023-08-25
# Runtime: 47 ms, Memory: 16.3 MB
# Submission Id: 1031098804


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        len1, len2, len3 = len(s1), len(s2), len(s3)
        if len3 != len1 + len2:
            return False
        
        dp = [[False] * (len2+1) for _ in range(len1+1)]
        dp[0][0] = True
        
        for p1 in range(len1):
            if s1[p1] != s3[p1]:
                break
            dp[p1+1][0] = True
            
        for p2 in range(len2):
            if s2[p2] != s3[p2]:
                break
            dp[0][p2+1] = True

        for p1 in range(len1):
            for p2 in range(len2):
                dp[p1+1][p2+1] = (
                    (dp[p1][p2+1] and s1[p1] == s3[p1+p2+1]) or
                    (dp[p1+1][p2] and s2[p2] == s3[p1+p2+1])
                )
                
        return dp[-1][-1]
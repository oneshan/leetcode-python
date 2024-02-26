# 0097 - Interleaving String
# Date: 2022-07-02
# Runtime: 77 ms, Memory: 14 MB
# Submission Id: 736618992


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n1 + n2 != n3:
            return False
        
        dp = [[False] * (n2+1) for _ in range(n1+1)]
        dp[0][0] = True
        
        for i in range(n1):
            dp[i+1][0] = dp[i][0] and s1[i] == s3[i]
        
        for j in range(n2):
            dp[0][j+1] = dp[0][j] and s2[j] == s3[j]
            
        for i in range(n1):
            for j in range(n2):
                dp[i+1][j+1] = (
                    (dp[i][j+1] and s1[i] == s3[i+j+1]) or
                    (dp[i+1][j] and s2[j] == s3[i+j+1]) 
                )
        
        return dp[-1][-1]
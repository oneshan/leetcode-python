# 0097 - Interleaving String
# Date: 2024-05-05
# Runtime: 51 ms, Memory: 16.6 MB
# Submission Id: 1249820920


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[False] * (len(s2)+1) for _ in range(len(s1)+1)]
        dp[0][0] = True
        
        for i in range(1, len(s1)+1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        for i in range(1, len(s2)+1):
            dp[0][i] = dp[0][i-1] and s2[i-1] == s3[i-1]

        for i in range(1, len(s1)+1):
            for j in range(1, len(s2)+1):
                res = False
                if s1[i-1] == s3[i+j-1]:
                    res |= dp[i-1][j]
                if s2[j-1] == s3[i+j-1]:
                    res |= dp[i][j-1]
                dp[i][j] = res

        return dp[-1][-1]
# 0097 - Interleaving String
# Date: 2024-05-27
# Runtime: 50 ms, Memory: 16.7 MB
# Submission Id: 1269159024


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[False] * (1 + len(s2)) for _ in range(1 + len(s1))]
        dp[0][0] = True
        for i in range(len(s2)):
            dp[0][i+1] = dp[0][i] and s2[i] == s3[i]
        for i in range(len(s1)):
            dp[i+1][0] = dp[i][0] and s1[i] == s3[i]

        for i in range(len(s1)):
            for j in range(len(s2)):
                if s1[i] == s3[i+j+1]:
                    dp[i+1][j+1] |= dp[i][j+1]
                if s2[j] == s3[i+j+1]:
                    dp[i+1][j+1] |= dp[i+1][j]

        return dp[-1][-1]
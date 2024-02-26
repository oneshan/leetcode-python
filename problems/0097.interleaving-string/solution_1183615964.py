# 0097 - Interleaving String
# Date: 2024-02-23
# Runtime: 43 ms, Memory: 16.6 MB
# Submission Id: 1183615964


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        dp = [False] * (len(s2)+1)
        dp[0] = True

        for p2 in range(len(s2)):
            if s2[p2] != s3[p2]:
                break
            dp[p2+1] = True

        for p1 in range(len(s1)):
            dp[0] = dp[0] and s1[p1] == s3[p1]
            for p2 in range(len(s2)):
                dp[p2+1] = (
                    (dp[p2+1] and s1[p1] == s3[p1+p2+1]) or
                    (dp[p2] and s2[p2] == s3[p1+p2+1])
                )

        return dp[-1]
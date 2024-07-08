# 0097 - Interleaving String
# Date: 2024-05-27
# Runtime: 51 ms, Memory: 16.5 MB
# Submission Id: 1269168137


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [False] * (1 + len(s2))
        dp[0] = True
        for j in range(len(s2)):
            dp[j+1] = dp[j] and s2[j] == s3[j]

        for i in range(len(s1)):
            dp[0] = dp[0] and s1[i] == s3[i]
            for j in range(len(s2)):
                dp[j+1] = (
                    (s1[i] == s3[i+j+1] and dp[j+1])
                    or (s2[j] == s3[i+j+1] and dp[j])
                )
        return dp[-1]
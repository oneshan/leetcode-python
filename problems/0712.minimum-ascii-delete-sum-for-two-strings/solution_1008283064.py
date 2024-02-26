# 0712 - Minimum ASCII Delete Sum for Two Strings
# Date: 2023-07-31
# Runtime: 456 ms, Memory: 20.9 MB
# Submission Id: 1008283064


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n1, n2 = len(s1), len(s2)
        
        dp = [[0] * (n2+1) for _ in range(n1+1)]
        
        for i in range(n1):
            dp[i+1][0] = dp[i][0] + ord(s1[i])
        for j in range(n2):
            dp[0][j+1] = dp[0][j] + ord(s2[j])
        
        for j in range(n2):
            for i in range(n1):
                if s1[i] == s2[j]:
                    dp[i+1][j+1] = dp[i][j]
                else:
                    dp[i+1][j+1] = min(dp[i+1][j] + ord(s2[j]),
                                       dp[i][j+1] + ord(s1[i]))
        return dp[-1][-1]
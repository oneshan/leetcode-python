# 0115 - Distinct Subsequences
# Date: 2024-05-27
# Runtime: 191 ms, Memory: 16.6 MB
# Submission Id: 1269180013


class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        dp = [0] * (1 + len(t))
        dp[0] = 1
        for i in range(len(s)):
            next_dp = dp[:]
            for j in range(len(t)):
                if s[i] == t[j]:
                    next_dp[j+1] += dp[j]
            dp = next_dp

        return dp[-1]
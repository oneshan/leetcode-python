# 1250 - Longest Common Subsequence
# Date: 2024-04-11
# Runtime: 328 ms, Memory: 16.6 MB
# Submission Id: 1229240112


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text2)
        
        prev = [0] * (n+1)
        for ch in text1:
            dp = [0] * (n+1)
            for i in range(n):
                if text2[i] == ch:
                    dp[i+1] = 1 + prev[i]
                else:
                    dp[i+1] = max(dp[i], prev[i+1])
            prev = dp
        return dp[-1]
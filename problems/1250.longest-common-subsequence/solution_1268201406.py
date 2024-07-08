# 1250 - Longest Common Subsequence
# Date: 2024-05-26
# Runtime: 426 ms, Memory: 16.6 MB
# Submission Id: 1268201406


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1, n2 = len(text1), len(text2)
        dp = [0] * (n2+1)
        
        for i in range(1, n1+1):
            next_dp = [0] * (n2+1)
            for j in range(1, n2+1):
                if text1[i-1] == text2[j-1]:
                    next_dp[j] = 1 + dp[j-1]
                else:
                    next_dp[j] = max(next_dp[j-1], dp[j])
            dp = next_dp
        return dp[-1]
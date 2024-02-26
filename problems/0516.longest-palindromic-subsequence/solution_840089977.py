# 0516 - Longest Palindromic Subsequence
# Date: 2022-11-09
# Runtime: 9031 ms, Memory: 39.3 MB
# Submission Id: 840089977


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        
        dp = [[0] * (n+1) for _ in range(n+1)]
        for i in range(n):
            for j in range(n):
                if s[i] == s[-j-1]:
                    dp[i+1][j+1] = 1 + dp[i][j]
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        return dp[-1][-1]
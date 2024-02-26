# 1178 - Valid Palindrome III
# Date: 2022-11-03
# Runtime: 1108 ms, Memory: 21.1 MB
# Submission Id: 835956037


class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        n = len(s)
        dp = [[0] * (n+1) for _ in range(n+1)]
        for i in range(n):
            dp[i][0] = i
            dp[0][i] = i
            
        for i in range(1, n+1):
            for j in range(1, n+1):
                if s[i-1] == s[-j]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1
        return dp[-1][-1] <= k * 2
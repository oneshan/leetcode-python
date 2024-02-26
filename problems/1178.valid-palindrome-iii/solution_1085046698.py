# 1178 - Valid Palindrome III
# Date: 2023-10-27
# Runtime: 200 ms, Memory: 18.3 MB
# Submission Id: 1085046698


class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n-1, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        
        return len(s) - dp[0][-1] <= k
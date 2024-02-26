# 1178 - Valid Palindrome III
# Date: 2023-10-27
# Runtime: 172 ms, Memory: 16.1 MB
# Submission Id: 1085048495


class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        
        n = len(s)
        prev_dp = [0] * n
        for i in range(n-1, -1, -1):
            dp = [0] * n
            dp[i] = 1
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[j] = prev_dp[j-1] + 2
                else:
                    dp[j] = max(dp[j-1], prev_dp[j])
            prev_dp = dp
        
        return len(s) - dp[-1] <= k
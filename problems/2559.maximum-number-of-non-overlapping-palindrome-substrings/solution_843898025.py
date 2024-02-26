# 2559 - Maximum Number of Non-overlapping Palindrome Substrings
# Date: 2022-11-15
# Runtime: 43 ms, Memory: 13.8 MB
# Submission Id: 843898025


class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        def is_palindrome(left, right):
            if left < 0:
                return False
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        dp = [0] * (n+1)
        for i in range(k, n+1):
            dp[i] = dp[i-1]
            if is_palindrome(i-k, i-1):
                dp[i] = max(dp[i], 1+dp[i-k])
            if is_palindrome(i-k-1, i-1):
                dp[i] = max(dp[i], 1+dp[i-k-1])
        return dp[-1]

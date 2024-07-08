# 0647 - Palindromic Substrings
# Date: 2024-05-27
# Runtime: 302 ms, Memory: 24.3 MB
# Submission Id: 1268973305


class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0

        n = len(s)
        ans = 0

        # dp[left][right]
        dp = [[False] * n for _ in range(n)]
        for size in range(1, n+1):
            for i in range(n-size+1):
                if s[i] == s[i+size-1] and (size <= 2 or dp[i+1][i+size-2]):
                    dp[i][i+size-1] = True
                    ans += 1

        return ans
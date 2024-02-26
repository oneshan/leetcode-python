# 2577 - Count Palindromic Subsequences
# Date: 2022-11-27
# Runtime: 2917 ms, Memory: 14 MB
# Submission Id: 850697915


class Solution:
    def countPalindromes(self, s: str) -> int:
        mod = 10**9 + 7
        ans = 0
        for i in range(10):
            for j in range(10):
                pattern = f'{i}{j}#{j}{i}'
                dp = [0, 0, 0, 0, 0, 1]
                for ch in s:
                    if ch == pattern[0]: dp[0] += dp[1]
                    if ch == pattern[1]: dp[1] += dp[2]
                    dp[2] += dp[3]
                    if ch == pattern[3]: dp[3] += dp[4]
                    if ch == pattern[4]: dp[4] += dp[5]
                ans += dp[0]
        return ans % mod
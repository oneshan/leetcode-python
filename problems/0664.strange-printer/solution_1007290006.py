# 0664 - Strange Printer
# Date: 2023-07-30
# Runtime: 414 ms, Memory: 16.5 MB
# Submission Id: 1007290006


class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        dp = [[n] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        
        for length in range(2, n+1):
            for left in range(n-length+1):
                right = left + length - 1
                dp[left][right] = 1 + dp[left+1][right]
                for i in range(left+1, right+1):
                    if s[left] == s[i]:
                        dp[left][right] = min(dp[left][right], dp[left][i-1] + (dp[i+1][right] if right > i else 0))
        return dp[0][n-1]       
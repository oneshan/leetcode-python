# 0664 - Strange Printer
# Date: 2023-07-30
# Runtime: 1359 ms, Memory: 16.5 MB
# Submission Id: 1007284964


class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        dp = [[n] * n for _ in range(n)]
        for length in range(1, n+1):
            for left in range(n-length+1):
                right = left + length - 1
                j = -1
                for i in range(left, right):
                    if s[i] != s[right] and j == -1:
                        j = i
                    if j != -1:
                        dp[left][right] = min(dp[left][right], 1 + dp[j][i] + dp[i+1][right])
                if j == -1:
                    dp[left][right] = 0
                    
        return 1 + dp[0][-1]
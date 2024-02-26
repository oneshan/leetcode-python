# 0279 - Perfect Squares
# Date: 2024-02-08
# Runtime: 2513 ms, Memory: 16.7 MB
# Submission Id: 1169362173


class Solution:
    def numSquares(self, n: int) -> int:
        square = [i * i for i in range(0, 101)]

        dp = [n] * (n+1)
        dp[0] = 0
        for i in range(n+1):
            for s in square:
                if i + s > n:
                    break
                dp[i+s] = min(dp[i+s], 1 + dp[i])

        return dp[-1]
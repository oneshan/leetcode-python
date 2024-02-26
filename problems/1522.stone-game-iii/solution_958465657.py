# 1522 - Stone Game III
# Date: 2023-05-28
# Runtime: 2395 ms, Memory: 21.1 MB
# Submission Id: 958465657


class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] * 4
        for i in range(n-1, -1, -1):
            dp[i % 4] = stoneValue[i] - dp[(i + 1) % 4]
            if i + 2 <= n:
                dp[i % 4] = max(dp[i % 4], stoneValue[i] + stoneValue[i+1] - dp[(i+2) % 4])
            if i + 3 <= n:
                dp[i % 4] = max(dp[i % 4],
                                stoneValue[i] + stoneValue[i+1] + stoneValue[i+2] - dp[(i+3) % 4])
        
        if dp[0] > 0:
            return "Alice"
        if dp[0] < 0:
            return "Bob"
        return "Tie"
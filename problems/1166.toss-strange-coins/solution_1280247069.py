# 1166 - Toss Strange Coins
# Date: 2024-06-07
# Runtime: 361 ms, Memory: 16.8 MB
# Submission Id: 1280247069


class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        dp = [0] * (target+1)
        dp[0] = 1

        for p in prob:
            for i in range(target, 0, -1):
                dp[i] = (1-p) * dp[i] + p * dp[i-1]
            dp[0] = dp[0] * (1-p)
        return dp[-1]
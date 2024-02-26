# 0867 - New 21 Game
# Date: 2022-10-17
# Runtime: 145 ms, Memory: 14.3 MB
# Submission Id: 824420570


class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or k + maxPts - 1 <= n:
            return 1
        
        dp = [0] * (n+1)
        dp[0] = 1
        
        curr = 1  # sliding window sum(dp[max(0,i-maxPts):min(i,k)])
        for i in range(1, n+1):
            # dp[i] = (sliding window sum) * (1/maxPts)
            dp[i] = curr / maxPts
            if i < k:
                curr += dp[i]
            if i >= maxPts:
                curr -= dp[i-maxPts]
        return sum(dp[k:])
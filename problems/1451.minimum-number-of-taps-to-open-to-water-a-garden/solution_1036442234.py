# 1451 - Minimum Number of Taps to Open to Water a Garden
# Date: 2023-08-31
# Runtime: 470 ms, Memory: 16.7 MB
# Submission Id: 1036442234


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        for i, radius in enumerate(ranges):
            _from, _to = max(0, i-radius), min(n, i+radius)
            for j in range(_from, _to+1):
                dp[_to] = min(dp[_to], dp[j] + 1)
        
        return -1 if dp[-1] == float('inf') else dp[-1]
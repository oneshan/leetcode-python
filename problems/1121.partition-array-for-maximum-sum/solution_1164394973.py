# 1121 - Partition Array for Maximum Sum
# Date: 2024-02-03
# Runtime: 276 ms, Memory: 16.5 MB
# Submission Id: 1164394973


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n+1)
        
        for i in range(1, n+1):
            curr_max = 0
            for j in range(1, min(i, k)+1):
                curr_max = max(curr_max, arr[i-j])
                dp[i] = max(dp[i], dp[i-j] + curr_max * j)
        return dp[-1]
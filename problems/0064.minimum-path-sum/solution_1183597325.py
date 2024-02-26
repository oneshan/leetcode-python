# 0064 - Minimum Path Sum
# Date: 2024-02-23
# Runtime: 76 ms, Memory: 17 MB
# Submission Id: 1183597325


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        len_r, len_c = len(grid), len(grid[0])
        
        dp = [0] * len_c
        dp[0] = grid[0][0]
        for c in range(1, len_c):
            dp[c] = dp[c-1] + grid[0][c]

        for r in range(1, len_r):
            dp[0] += grid[r][0]
            for c in range(1, len_c):
                dp[c] = min(dp[c], dp[c-1]) + grid[r][c]

        return dp[-1]
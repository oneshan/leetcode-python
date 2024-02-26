# 0064 - Minimum Path Sum
# Date: 2022-11-07
# Runtime: 248 ms, Memory: 14.7 MB
# Submission Id: 838692848


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
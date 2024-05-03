# 0064 - Minimum Path Sum
# Date: 2024-05-02
# Runtime: 89 ms, Memory: 17.2 MB
# Submission Id: 1247240245


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        len_r, len_c = len(grid), len(grid[0])
        
        dp = [0] * len_c
        curr = 0
        for c in range(len_c):
            curr += grid[0][c]
            dp[c] = curr
        
        for r in range(1, len_r):
            dp[0] += grid[r][0]
            for c in range(1, len_c):
                dp[c] = min(dp[c], dp[c-1]) + grid[r][c]
        
        return dp[-1]
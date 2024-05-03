# 0064 - Minimum Path Sum
# Date: 2024-05-02
# Runtime: 82 ms, Memory: 22.4 MB
# Submission Id: 1247242119


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        len_r, len_c = len(grid), len(grid[0])
        
        @cache
        def dp(r, c):
            if r < 0 or c < 0:
                return 0
            if r == 0:
                return dp(r, c-1) + grid[0][c]
            if c == 0:
                return dp(r-1, c) + grid[r][0]
            return min(dp(r-1, c), dp(r, c-1)) + grid[r][c]
        
        return dp(len_r-1, len_c-1)
# 3391 - Maximum Difference Score in a Grid
# Date: 2024-05-12
# Runtime: 1166 ms, Memory: 27.2 MB
# Submission Id: 1255907688


class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        len_r, len_c = len(grid), len(grid[0])
        
        ans = float('-inf')
        for r in range(len_r):
            for c in range(len_c):
                if r:
                    ans = max(ans, grid[r][c] - grid[r-1][c])
                if c:
                    ans = max(ans, grid[r][c] - grid[r][c-1])
                if r:
                    grid[r][c] = min(grid[r][c], grid[r-1][c])
                if c:
                    grid[r][c] = min(grid[r][c], grid[r][c-1])
        return ans
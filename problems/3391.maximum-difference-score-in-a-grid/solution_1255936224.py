# 3391 - Maximum Difference Score in a Grid
# Date: 2024-05-12
# Runtime: 1024 ms, Memory: 27.1 MB
# Submission Id: 1255936224


class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        len_r, len_c = len(grid), len(grid[0])
        
        ans = float('-inf')
        for r in range(len_r):
            for c in range(len_c):
                prev_min = min(
                    grid[r-1][c] if r else float('inf'),
                    grid[r][c-1] if c else float('inf'),
                )
                ans = max(ans, grid[r][c] - prev_min)
                grid[r][c] = min(grid[r][c], prev_min)
        return ans
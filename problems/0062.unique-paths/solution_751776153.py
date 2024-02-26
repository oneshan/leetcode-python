# 0062 - Unique Paths
# Date: 2022-07-20
# Runtime: 58 ms, Memory: 13.9 MB
# Submission Id: 751776153


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0] * n for _ in range(m)]
        
        for r in range(m):
            grid[r][0] = 1
        for c in range(n):
            grid[0][c] = 1
            
        for r in range(1, m):
            for c in range(1, n):
                grid[r][c] = grid[r-1][c] + grid[r][c-1]
        
        return grid[-1][-1]
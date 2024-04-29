# 1224 - Minimum Falling Path Sum II
# Date: 2024-04-26
# Runtime: 215 ms, Memory: 20.1 MB
# Submission Id: 1242143968


class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)

        for r in range(1, n):
            min1 = min2 = float('inf')
            for num in grid[r-1]:
                if num <= min1:
                    min1, min2 = num, min1
                elif num < min2:
                    min2 = num
            for c in range(n):
                grid[r][c] += min2 if grid[r-1][c] == min1 else min1

        return min(grid[-1])
# 0064 - Minimum Path Sum
# Date: 2023-03-27
# Runtime: 102 ms, Memory: 15.8 MB
# Submission Id: 922755082


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        len_r, len_c = len(grid), len(grid[0])
        
        for col in range(1, len_c):
            grid[0][col] += grid[0][col-1]
        for row in range(1, len_r):
            grid[row][0] += grid[row-1][0]
        
        for row in range(1, len_r):
            for col in range(1, len_c):
                grid[row][col] += min(grid[row-1][col], grid[row][col-1])
        return grid[-1][-1]
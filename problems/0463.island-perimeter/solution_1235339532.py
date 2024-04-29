# 0463 - Island Perimeter
# Date: 2024-04-18
# Runtime: 362 ms, Memory: 16.9 MB
# Submission Id: 1235339532


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        len_r, len_c = len(grid), len(grid[0])
        ans = 0
        for r in range(len_r):
            for c in range(len_c):
                if grid[r][c] == 1:
                    ans += (r == 0 or grid[r-1][c] == 0)
                    ans += (r == len_r -1 or grid[r+1][c] == 0)
                    ans += (c == 0 or grid[r][c-1] == 0)
                    ans += (c == len_c -1 or grid[r][c+1] == 0)
        return ans
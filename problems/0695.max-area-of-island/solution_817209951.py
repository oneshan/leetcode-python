# 0695 - Max Area of Island
# Date: 2022-10-07
# Runtime: 150 ms, Memory: 17.8 MB
# Submission Id: 817209951


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        len_r, len_c = len(grid), len(grid[0])
        seen = set()
        
        def dfs(x, y):
            if grid[x][y] == 0 or (x,y) in seen:
                return 0
            seen.add((x,y))
            area = 1
            if x > 0:
                area += dfs(x-1, y)
            if y > 0:
                area += dfs(x, y-1)
            if x < len_r-1:
                area += dfs(x+1, y)
            if y < len_c-1:
                area += dfs(x, y+1)
            return area
        
        ans = 0
        for r in range(len_r):
            for c in range(len_c):
                if grid[r][c]:
                    ans = max(ans, dfs(r,c))
        return ans
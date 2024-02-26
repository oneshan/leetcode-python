# 0200 - Number of Islands
# Date: 2022-10-04
# Runtime: 826 ms, Memory: 22 MB
# Submission Id: 815089156


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        seen = set()
        
        def dfs(x, y):
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dx, dy in directions:
                new_x, new_y = x+dx, y+dy
                if (new_x, new_y) in seen:
                    continue
                if 0 <= new_x < n and 0 <= new_y < m and grid[new_x][new_y] == '1':
                    seen.add((new_x, new_y))
                    dfs(new_x, new_y)
        
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and (i,j) not in seen:
                    ans += 1
                    seen.add((i, j))
                    dfs(i, j)
        return ans
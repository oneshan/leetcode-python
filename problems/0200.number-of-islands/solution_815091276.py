# 0200 - Number of Islands
# Date: 2022-10-04
# Runtime: 773 ms, Memory: 16.5 MB
# Submission Id: 815091276


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        
        def dfs(x, y):
            if grid[x][y] == '1':
                grid[x][y] = '0'
                if x > 0: dfs(x-1, y)
                if y > 0: dfs(x, y-1)
                if x < n-1: dfs(x+1, y)
                if y < m-1: dfs(x, y+1)

        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    ans += 1
                    dfs(i, j)
        return ans
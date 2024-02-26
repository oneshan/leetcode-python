# 0200 - Number of Islands
# Date: 2022-07-18
# Runtime: 337 ms, Memory: 16.4 MB
# Submission Id: 750318405


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        len_r, len_c = len(grid), len(grid[0])
        ans = 0
        
        def dfs(r, c):
            if grid[r][c] == '1':
                grid[r][c] = '0'
                if r > 0: dfs(r-1, c)
                if c > 0: dfs(r, c-1)
                if r < len_r -1: dfs(r+1, c)
                if c < len_c -1: dfs(r, c+1)
        
        for r in range(len_r):
            for c in range(len_c):
                if grid[r][c] != '1':
                    continue
                ans += 1
                dfs(r, c)
        
        return ans
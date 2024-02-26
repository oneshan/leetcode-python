# 0200 - Number of Islands
# Date: 2023-09-16
# Runtime: 264 ms, Memory: 18.7 MB
# Submission Id: 1050537723


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        len_r, len_c = len(grid), len(grid[0])
        ans = 0
        
        def dfs(r, c):
            stack = [(r, c)]
            while stack:
                r, c = stack.pop()
                for dr, dc in (0, 1), (0, -1), (1, 0), (-1, 0):
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < len_r and 0 <= nc < len_c and grid[nr][nc] == '1':
                        grid[nr][nc] = '0'
                        stack.append((nr, nc))
        
        for r in range(len_r):
            for c in range(len_c):
                if grid[r][c] == '0':
                    continue
                grid[r][c] = '0'
                ans += 1
                dfs(r, c)
        return ans
# 0200 - Number of Islands
# Date: 2024-05-20
# Runtime: 235 ms, Memory: 18.8 MB
# Submission Id: 1262828068


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        len_r, len_c = len(grid), len(grid[0])
        
        def traverse(r, c):
            grid[r][c] = '0'
            stack = [(r, c)]
            while stack:
                r, c = stack.pop()
                for nr, nc in (r+1, c), (r-1, c), (r, c+1), (r, c-1):
                    if 0 <= nr < len_r and 0 <= nc < len_c and grid[nr][nc] == '1':
                        grid[nr][nc] = '0'
                        stack.append((nr, nc))

        ans = 0
        for r in range(len_r):
            for c in range(len_c):
                if grid[r][c] == '1':
                    ans += 1
                    traverse(r, c)
        return ans
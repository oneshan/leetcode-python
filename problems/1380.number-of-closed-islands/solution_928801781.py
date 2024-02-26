# 1380 - Number of Closed Islands
# Date: 2023-04-06
# Runtime: 128 ms, Memory: 14.3 MB
# Submission Id: 928801781


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        len_r, len_c = len(grid), len(grid[0])
        count = 0
        
        def dfs(row, col):
            stack = [(row, col)]
            grid[row][col] = 1
            is_valid = 1
            while stack:
                r, c = stack.pop()
                if r in (0, len_r-1) or c in (0, len_c-1):
                    is_valid = 0
                for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
                    new_r, new_c = r+dx, c+dy
                    if (0 <= new_r < len_r
                            and 0 <= new_c < len_c
                            and grid[new_r][new_c] == 0):
                        grid[new_r][new_c] = 1
                        stack.append((new_r, new_c))
            return is_valid
        
        for r in range(len_r):
            for c in range(len_c):
                if grid[r][c] == 0:
                    count += dfs(r, c)
                    
        return count
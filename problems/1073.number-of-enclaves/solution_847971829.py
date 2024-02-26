# 1073 - Number of Enclaves
# Date: 2022-11-22
# Runtime: 816 ms, Memory: 17.4 MB
# Submission Id: 847971829


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        len_r, len_c = len(grid), len(grid[0])
        count = 0
        
        def dfs(row, col):
            stack = [(row, col)]
            count = 1
            while stack:
                r, c = stack.pop()
                if r in (0, len_r-1) or c in (0, len_c-1):
                    count = float('-inf')
                for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
                    new_r, new_c = r+dx, c+dy
                    if (0 <= new_r < len_r and 0 <= new_c < len_c
                            and grid[new_r][new_c] == 1):
                        count += 1
                        stack.append((new_r, new_c))
                        grid[new_r][new_c] = 0
            return count if count != float('-inf') else 0
        
        for r in range(len_r):
            for c in range(len_c):
                if grid[r][c] == 1:
                    grid[r][c] = 0
                    count += dfs(r, c)

        return count
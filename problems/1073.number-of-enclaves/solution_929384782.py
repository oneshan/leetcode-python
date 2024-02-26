# 1073 - Number of Enclaves
# Date: 2023-04-07
# Runtime: 763 ms, Memory: 17.5 MB
# Submission Id: 929384782


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        len_r, len_c = len(grid), len(grid[0])
        ans = 0
        
        def dfs(row, col):
            count = 1
            is_boundary = False
            stack = [(row, col)]
            while stack:
                r, c = stack.pop()
                if r in (0, len_r-1) or c in (0, len_c-1):
                    is_boundary = True
                for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    new_r, new_c = r + dx, c + dy
                    if len_r > new_r >= 0 and len_c > new_c >= 0 and grid[new_r][new_c] == 1:
                        grid[new_r][new_c] = 0
                        count += 1
                        stack.append((new_r, new_c))
            return 0 if is_boundary else count
        
        
        for r in range(len_r):
            for c in range(len_c):
                if grid[r][c]:
                    grid[r][c] = 0
                    ans += dfs(r, c)
        return ans
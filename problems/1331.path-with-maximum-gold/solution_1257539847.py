# 1331 - Path with Maximum Gold
# Date: 2024-05-14
# Runtime: 2021 ms, Memory: 16.8 MB
# Submission Id: 1257539847


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        len_r, len_c = len(grid), len(grid[0])

        def dfs(r, c):
            if not (0 <= r < len_r) or not (0 <= c < len_c) or grid[r][c] == 0:
                return 0
            
            tmp = grid[r][c]
            grid[r][c] = 0
            res = tmp + max(dfs(r+1, c), dfs(r, c+1), dfs(r-1, c), dfs(r, c-1))
            grid[r][c] = tmp
            return res

        ans = 0
        for r in range(len_r):
            for c in range(len_c):
                if grid[r][c]:
                    ans = max(ans, dfs(r, c))
        return ans
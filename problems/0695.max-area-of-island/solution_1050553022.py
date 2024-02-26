# 0695 - Max Area of Island
# Date: 2023-09-16
# Runtime: 127 ms, Memory: 19.7 MB
# Submission Id: 1050553022


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        len_r, len_c = len(grid), len(grid[0])
        seen = set()
        ans = 0
        
        def dfs(r, c):
            if not (0 <= r < len_r and 0 <= c < len_c
                    and (r, c) not in seen and grid[r][c]):
                return 0
            seen.add((r, c))
            return 1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c-1) + dfs(r, c+1)
        
        for r in range(len_r):
            for c in range(len_c):
                ans = max(ans, dfs(r, c))
        return ans
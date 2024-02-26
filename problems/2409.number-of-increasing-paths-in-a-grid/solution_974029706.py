# 2409 - Number of Increasing Paths in a Grid
# Date: 2023-06-18
# Runtime: 2122 ms, Memory: 141.6 MB
# Submission Id: 974029706


class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        len_r, len_c = len(grid), len(grid[0])
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        
        @cache
        def dp(r, c):
            count = 1
            for dx, dy in directions:
                prev_r, prev_c = r + dx, c + dy
                if 0 <= prev_r < len_r and 0 <= prev_c < len_c and grid[r][c] > grid[prev_r][prev_c]:
                    count += dp(prev_r, prev_c) % mod
            return count
        
        ans = 0
        for i in range(len_r):
            for j in range(len_c):
                ans += dp(i, j) % mod
        return ans % mod
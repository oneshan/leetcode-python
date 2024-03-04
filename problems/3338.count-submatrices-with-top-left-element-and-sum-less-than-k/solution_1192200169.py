# 3338 - Count Submatrices with Top-Left Element and Sum Less Than k
# Date: 2024-03-03
# Runtime: 1608 ms, Memory: 65.9 MB
# Submission Id: 1192200169


class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        if grid[0][0] > k:
            return 0

        len_r, len_c = len(grid), len(grid[0])
        for r in range(len_r):
            for c in range(1, len_c):
                grid[r][c] += grid[r][c-1]
        
        ans = 0
        for r in range(len_r):
            for c in range(len_c):
                if r > 0:
                    grid[r][c] += grid[r-1][c]
                if grid[r][c] <= k:
                    ans += 1
        return ans
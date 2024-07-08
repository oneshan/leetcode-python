# 0891 - Score After Flipping Matrix
# Date: 2024-05-13
# Runtime: 35 ms, Memory: 16.4 MB
# Submission Id: 1256659813


class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        len_r, len_c = len(grid), len(grid[0])

        ans = 0
        for c in range(len_c):
            count = sum(grid[r][c] == grid[r][0] for r in range(len_r))
            ans += max(count, len_r-count) << (len_c - c - 1)

        return ans
# 0891 - Score After Flipping Matrix
# Date: 2024-05-13
# Runtime: 49 ms, Memory: 16.2 MB
# Submission Id: 1256620474


class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        len_r, len_c = len(grid), len(grid[0])

        for r in range(len_r):
            if grid[r][0] == 0:
                for c in range(len_c):
                    grid[r][c] ^= 1
        
        ans = 0
        for c in range(len_c):
            count = sum(grid[r][c] for r in range(len_r))
            ans += max(count, len_r-count) << (len_c - c - 1)
        return ans
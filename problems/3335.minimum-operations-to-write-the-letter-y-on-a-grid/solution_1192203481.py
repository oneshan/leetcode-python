# 3335 - Minimum Operations to Write the Letter Y on a Grid
# Date: 2024-03-03
# Runtime: 349 ms, Memory: 16.6 MB
# Submission Id: 1192203481


class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        len_r, len_c = len(grid), len(grid[0])
        half = len_r >> 1

        count_y = [0, 0, 0]
        count_n = [0, 0, 0]
            
        for r in range(len_r):
            for c in range(len_c):
                if (r < half and (r == c or r + c == len_r - 1)) or (r >= half and c == half):
                    count_y[grid[r][c]] += 1
                else:
                    count_n[grid[r][c]] += 1
        
        total = len_r * len_c
        ans = float('inf')
        for i in range(3):
            for j in range(3):
                if i == j:
                    continue
                ans = min(ans, total - count_y[i] - count_n[j])
        return ans
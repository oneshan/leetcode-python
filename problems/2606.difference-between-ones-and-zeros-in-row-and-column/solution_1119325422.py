# 2606 - Difference Between Ones and Zeros in Row and Column
# Date: 2023-12-14
# Runtime: 1367 ms, Memory: 51.7 MB
# Submission Id: 1119325422


class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        len_r, len_c = len(grid), len(grid[0])
        rows = [0] * len_r
        cols = [0] * len_c
        
        ans = [[0] * len_c for _ in range(len_r)]
        
        for r in range(len_r):
            for c in range(len_c):
                if grid[r][c]:
                    rows[r] += 1
                    cols[c] += 1
        
        for r in range(len_r):
            for c in range(len_c):
                ans[r][c] = rows[r] + cols[c] - (len_r - rows[r]) - (len_c - cols[c])
        return ans
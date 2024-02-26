# 2606 - Difference Between Ones and Zeros in Row and Column
# Date: 2022-11-26
# Runtime: 5088 ms, Memory: 48.1 MB
# Submission Id: 850117042


class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        len_r, len_c = len(grid), len(grid[0])
        
        row_0 = [0] * len_r
        row_1 = [0] * len_r
        col_0 = [0] * len_c
        col_1 = [0] * len_c
        
        for r in range(len_r):
            for c in range(len_c):
                if grid[r][c] == 1:
                    row_1[r] += 1
                    col_1[c] += 1
                else:
                    row_0[r] += 1
                    col_0[c] += 1
                    
        ans = [[0] * len_c for _ in range(len_r)]
        for r in range(len_r):
            for c in range(len_c):
                ans[r][c] = row_1[r] + col_1[c] - row_0[r] - col_0[c]
        return ans
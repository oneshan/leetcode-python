# 3031 - Construct Product Matrix
# Date: 2023-10-15
# Runtime: 1178 ms, Memory: 50.1 MB
# Submission Id: 1075603364


class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        len_r, len_c = len(grid), len(grid[0])
        n = len_r * len_c
        
        ans = [[1] * len_c for _ in range(len_r)]
        for i in range(1, n):
            r, c = divmod(i, len_c)
            if c:
                ans[r][c] = grid[r][c-1] * ans[r][c-1] % MOD
            else:
                ans[r][c] = grid[r-1][-1] * ans[r-1][-1] % MOD
        
        right = 1
        for i in range(n-1, -1, -1):
            r, c = divmod(i, len_c)
            ans[r][c] = ans[r][c] * right % MOD
            right *= grid[r][c] % MOD
            
        return ans
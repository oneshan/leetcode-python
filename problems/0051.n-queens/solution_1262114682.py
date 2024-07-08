# 0051 - N-Queens
# Date: 2024-05-19
# Runtime: 49 ms, Memory: 17 MB
# Submission Id: 1262114682


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        puzzle = [['.'] * n for _ in range(n)]

        def backtrack(puzzle, r, cols, diags, anti_diags):
            if r == n:
                arr = [''.join(p) for p in puzzle]
                ans.append(arr)
                return
            for c in range(n):
                mask_c = 1 << c
                mask_d = 1 << (n+r-c)
                mask_a = 1 << (c+r)
                if mask_c & cols or mask_d & diags or mask_a & anti_diags:
                    continue
                puzzle[r][c] = 'Q'
                backtrack(puzzle, r+1, cols | mask_c, diags | mask_d, anti_diags | mask_a)
                puzzle[r][c] = '.'

        backtrack(puzzle, 0, 0, 0, 0)
        return ans
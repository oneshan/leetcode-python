# 0073 - Set Matrix Zeroes
# Date: 2024-05-23
# Runtime: 107 ms, Memory: 17.4 MB
# Submission Id: 1265523295


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        len_r, len_c = len(matrix), len(matrix[0])
        rows = cols = 0
        for r in range(len_r):
            for c in range(len_c):
                if matrix[r][c] == 0:
                    rows |= (1 << r)
                    cols |= (1 << c)

        for r in range(len_r):
            if rows & (1 << r) == 0:
                continue
            for c in range(len_c):
                matrix[r][c] = 0

        for c in range(len_c):
            if cols & (1 << c) == 0:
                continue
            for r in range(len_r):
                matrix[r][c] = 0
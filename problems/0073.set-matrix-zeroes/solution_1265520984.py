# 0073 - Set Matrix Zeroes
# Date: 2024-05-23
# Runtime: 114 ms, Memory: 17.5 MB
# Submission Id: 1265520984


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
            for c in range(len_c):
                if rows & (1 << r):
                    matrix[r][c] = 0
                if cols & (1 << c):
                    matrix[r][c] = 0
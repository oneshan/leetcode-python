# 0073 - Set Matrix Zeroes
# Date: 2024-02-21
# Runtime: 99 ms, Memory: 17.5 MB
# Submission Id: 1181628281


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        len_r, len_c = len(matrix), len(matrix[0])
        zero_r = zero_c = 0
        for r in range(len_r):
            for c in range(len_c):
                if matrix[r][c] == 0:
                    zero_r |= 1 << r
                    zero_c |= 1 << c
        
        for r in range(len_r):
            if zero_r & 1 << r:
                for c in range(len_c):
                    matrix[r][c] = 0
        
        for c in range(len_c):
            if zero_c & 1 << c:
                for r in range(len_r):
                    matrix[r][c] = 0
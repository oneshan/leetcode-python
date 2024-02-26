# 3330 - Modify the Matrix
# Date: 2024-02-11
# Runtime: 85 ms, Memory: 16.8 MB
# Submission Id: 1171868816


class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        len_r, len_c = len(matrix), len(matrix[0])
        
        for c in range(len_c):
            max_c = 0
            for r in range(len_r):
                max_c = max(max_c, matrix[r][c])
            for r in range(len_r):
                if matrix[r][c] == -1:
                    matrix[r][c] = max_c
        return matrix
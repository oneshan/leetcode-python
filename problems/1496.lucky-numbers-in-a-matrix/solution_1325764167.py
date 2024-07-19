# 1496 - Lucky Numbers in a Matrix
# Date: 2024-07-19
# Runtime: 113 ms, Memory: 16.8 MB
# Submission Id: 1325764167


class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        len_r, len_c = len(matrix), len(matrix[0])
        idx_r = idx_c = -1

        for r in range(len_r):
            # min in row
            min_c = 0
            for c in range(1, len_c):
                if matrix[r][c] < matrix[r][min_c]:
                    min_c = c
            # max in col
            if idx_r == -1 or matrix[r][min_c] > matrix[idx_r][idx_c]:
                idx_r, idx_c = r, min_c

        for r in range(len_r):
            if matrix[r][idx_c] > matrix[idx_r][idx_c]:
                return []

        return [matrix[idx_r][idx_c]]
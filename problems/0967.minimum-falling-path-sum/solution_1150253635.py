# 0967 - Minimum Falling Path Sum
# Date: 2024-01-19
# Runtime: 108 ms, Memory: 18.3 MB
# Submission Id: 1150253635


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        len_r, len_c = len(matrix), len(matrix[0])
        
        for r in range(1, len_r):
            for c in range(len_c):
                next_min = matrix[r-1][c]
                if c > 0:
                    next_min = min(matrix[r-1][c-1], next_min)
                if c < len_r -1:
                    next_min = min(matrix[r-1][c+1], next_min)
                matrix[r][c] += next_min
        return min(matrix[-1])
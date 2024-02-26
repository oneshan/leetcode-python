# 0967 - Minimum Falling Path Sum
# Date: 2022-11-02
# Runtime: 314 ms, Memory: 14.7 MB
# Submission Id: 835272639


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        for row in range(1, n):
            for col in range(n):
                min_val = matrix[row-1][col]
                if col > 0:
                    min_val = min(min_val, matrix[row-1][col-1])
                if col < n-1:
                    min_val = min(min_val, matrix[row-1][col+1])
                matrix[row][col] += min_val
        return min(matrix[-1])
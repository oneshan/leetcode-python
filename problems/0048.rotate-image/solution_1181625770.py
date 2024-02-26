# 0048 - Rotate Image
# Date: 2024-02-21
# Runtime: 30 ms, Memory: 16.7 MB
# Submission Id: 1181625770


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)        
        for r in range(n):
            for c in range(r):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        for r in range(n):
            left, right = 0, n-1
            while left < right:
                matrix[r][left], matrix[r][right] = matrix[r][right], matrix[r][left]
                left += 1
                right -= 1
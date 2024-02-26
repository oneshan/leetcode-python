# 0048 - Rotate Image
# Date: 2023-10-08
# Runtime: 48 ms, Memory: 16.3 MB
# Submission Id: 1070218881


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
        for i in range(n):
            for j in range(n>>1):
                matrix[i][j], matrix[i][-j-1] = matrix[i][-j-1], matrix[i][j]

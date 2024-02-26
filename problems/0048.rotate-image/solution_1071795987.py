# 0048 - Rotate Image
# Date: 2023-10-10
# Runtime: 41 ms, Memory: 16.3 MB
# Submission Id: 1071795987


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        for i in range((n >> 1) + (n & 1)):
            for j in range(n >> 1):
                tmp = matrix[-j-1][i]
                matrix[-j-1][i] = matrix[-i-1][-j-1]
                matrix[-i-1][-j-1] = matrix[j][-i-1]
                matrix[j][-i-1] = matrix[i][j]
                matrix[i][j] = tmp
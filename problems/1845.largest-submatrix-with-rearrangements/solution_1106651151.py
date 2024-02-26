# 1845 - Largest Submatrix With Rearrangements
# Date: 2023-11-26
# Runtime: 1091 ms, Memory: 42.9 MB
# Submission Id: 1106651151


class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        len_r, len_c = len(matrix), len(matrix[0])
        
        for r in range(1, len_r):
            for c in range(len_c):
                if matrix[r][c] == 1:
                    matrix[r][c] += matrix[r-1][c]
        
        for r in range(len_r):
            matrix[r].sort(reverse=True)
        
        ans = 0
        for r in range(len_r):
            for c in range(len_c):
                ans = max(ans, matrix[r][c] * (c+1))
        
        return ans
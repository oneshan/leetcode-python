# 1845 - Largest Submatrix With Rearrangements
# Date: 2023-11-26
# Runtime: 1105 ms, Memory: 42.7 MB
# Submission Id: 1106637899


class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        len_r, len_c = len(matrix), len(matrix[0])
        
        ans = 0
        for r in range(len_r):
            for c in range(len_c):
                if matrix[r][c] == 1 and r > 0:
                    matrix[r][c] += matrix[r-1][c]
            
            row = sorted(matrix[r], reverse=True)
            for c in range(len_c):
                ans = max(ans, row[c] * (c+1))
        return ans
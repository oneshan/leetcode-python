# 0898 - Transpose Matrix
# Date: 2023-12-10
# Runtime: 74 ms, Memory: 17.1 MB
# Submission Id: 1116253196


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        len_r = len(matrix)
        len_c = len(matrix[0])
        
        ans = [[None] * len_r for _ in range(len_c)]
        for r in range(len_r):
            for c in range(len_c):
                ans[c][r] = matrix[r][c]
        return ans
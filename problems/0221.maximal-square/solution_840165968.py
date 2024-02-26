# 0221 - Maximal Square
# Date: 2022-11-09
# Runtime: 1463 ms, Memory: 16.9 MB
# Submission Id: 840165968


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        len_r, len_c = len(matrix), len(matrix[0])
        prev = [0] * len_c
        curr = [0] * len_c
        max_len = 0
        
        for r in range(len_r):
            curr[0] = 0 if matrix[r][0] == '0' else 1
            max_len = max(max_len, curr[0])
            for c in range(1, len_c):
                if matrix[r][c] == '0':
                    curr[c] = 0
                else:
                    curr[c] = min(curr[c-1], prev[c], prev[c-1]) + 1
                    max_len = max(max_len, curr[c])
            prev, curr = curr, prev

        return max_len * max_len
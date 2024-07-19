# 1496 - Lucky Numbers in a Matrix
# Date: 2024-07-19
# Runtime: 117 ms, Memory: 16.6 MB
# Submission Id: 1325754595


class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        len_r, len_c = len(matrix), len(matrix[0])

        min_in_rows = [float('inf')] * len_r
        max_in_cols = [float('-inf')] * len_c
        for r in range(len_r):
            for c in range(len_c):
                min_in_rows[r] = min(min_in_rows[r], matrix[r][c])
                max_in_cols[c] = max(max_in_cols[c], matrix[r][c])

        ans = []
        for r in range(len_r):
            for c in range(len_c):
                if matrix[r][c] == min_in_rows[r] == max_in_cols[c]:
                    ans.append(matrix[r][c])
        return ans
# 1496 - Lucky Numbers in a Matrix
# Date: 2024-07-19
# Runtime: 104 ms, Memory: 16.9 MB
# Submission Id: 1325763786


class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        len_r, len_c = len(matrix), len(matrix[0])

        min_max_r = float('-inf')
        for r in range(len_r):
            curr_min = min(matrix[r])
            min_max_r = max(min_max_r, curr_min)

        max_min_c = float('inf')
        for c in range(len_c):
            curr_max = max(matrix[r][c] for r in range(len_r))
            max_min_c = min(max_min_c, curr_max)
        
        if min_max_r == max_min_c:
            return [min_max_r]
        return []
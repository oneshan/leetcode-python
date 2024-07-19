# 1496 - Lucky Numbers in a Matrix
# Date: 2024-07-19
# Runtime: 112 ms, Memory: 16.8 MB
# Submission Id: 1325775981


class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        min_in_rows = {min(r) for r in matrix}
        max_in_cols = {max(c) for c in zip(*matrix)}
        return list(min_in_rows & max_in_cols)
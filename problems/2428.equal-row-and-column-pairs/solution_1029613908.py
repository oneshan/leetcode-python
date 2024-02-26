# 2428 - Equal Row and Column Pairs
# Date: 2023-08-23
# Runtime: 456 ms, Memory: 21.1 MB
# Submission Id: 1029613908


from collections import Counter

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        row_counter = Counter([tuple(row) for row in grid])

        ans = 0
        for c in range(n):
            col = tuple(grid[i][c] for i in range(n))
            ans += row_counter[tuple(col)]
        return ans
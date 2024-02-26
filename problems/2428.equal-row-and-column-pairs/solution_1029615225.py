# 2428 - Equal Row and Column Pairs
# Date: 2023-08-23
# Runtime: 423 ms, Memory: 21.8 MB
# Submission Id: 1029615225


from collections import defaultdict

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        table_row = defaultdict(int)
        for row in grid:
            table_row[tuple(row)] += 1
            
        table_col = defaultdict(int)
        for col in zip(*grid):
            table_col[tuple(col)] += 1
          
        ans = 0
        for key in table_col:
            ans += table_row[key] * table_col[key]
        return ans
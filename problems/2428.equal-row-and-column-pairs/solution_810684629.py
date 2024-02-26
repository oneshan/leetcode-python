# 2428 - Equal Row and Column Pairs
# Date: 2022-09-29
# Runtime: 1157 ms, Memory: 18.9 MB
# Submission Id: 810684629


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
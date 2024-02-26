# 2428 - Equal Row and Column Pairs
# Date: 2022-09-28
# Runtime: 1489 ms, Memory: 18.9 MB
# Submission Id: 810680357


from collections import Counter

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        rows = [0] * n
        cols = [0] * n
        for r in range(n):
            for c in range(n):
                num = grid[r][c]
                rows[r] = 10 * rows[r] + num
                cols[c] = 10 * cols[c] + num
        
        rows = Counter(rows)
        cols = Counter(cols)
        ans = 0
        for key, count in rows.items():
            ans += cols[key] * count
        return ans
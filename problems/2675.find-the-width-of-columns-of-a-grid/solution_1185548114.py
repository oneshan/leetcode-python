# 2675 - Find the Width of Columns of a Grid
# Date: 2024-02-25
# Runtime: 100 ms, Memory: 18.1 MB
# Submission Id: 1185548114


class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        len_r, len_c = len(grid), len(grid[0])
        ans = [0] * len_c
        for r in range(len_r):
            for c in range(len_c):
                ans[c] = max(ans[c], len(str(grid[r][c])))
        return ans
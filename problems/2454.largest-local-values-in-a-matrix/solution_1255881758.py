# 2454 - Largest Local Values in a Matrix
# Date: 2024-05-12
# Runtime: 138 ms, Memory: 17 MB
# Submission Id: 1255881758


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        len_r = len_c = len(grid)

        def get_max(r, c):
            res = 0
            for nr in range(r, r+3):
                for nc in range(c, c+3):
                    res = max(res, grid[nr][nc])
            return res

        ans = [[0] * (len_c-2) for _ in range(len_r-2)]
        for r in range(len_r -2):
            for c in range(len_c - 2):
                ans[r][c] = get_max(r, c)
        return ans
# 0329 - Longest Increasing Path in a Matrix
# Date: 2024-05-27
# Runtime: 506 ms, Memory: 52.7 MB
# Submission Id: 1269012548


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        len_r, len_c = len(matrix), len(matrix[0])

        @cache
        def dp(pr, pc, r, c):
            if not (0 <= r < len_r and 0 <= c < len_c):
                return 0
            res = 1
            for nr, nc in (r-1, c), (r+1, c), (r, c-1), (r, c+1):
                if 0 <= nr < len_r and 0 <= nc < len_c and matrix[r][c] > matrix[nr][nc]:
                    res = max(res, 1 + dp(r, c, nr, nc))
            return res

        ans = 0
        for r in range(len_r):
            for c in range(len_c):
                ans = max(ans, dp(-1, -1, r, c))
        return ans
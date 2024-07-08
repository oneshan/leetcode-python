# 0329 - Longest Increasing Path in a Matrix
# Date: 2024-05-27
# Runtime: 295 ms, Memory: 21 MB
# Submission Id: 1269013350


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        len_r, len_c = len(matrix), len(matrix[0])

        @cache
        def dp(r, c):
            if not (0 <= r < len_r and 0 <= c < len_c):
                return 0
            res = 0
            for nr, nc in (r-1, c), (r+1, c), (r, c-1), (r, c+1):
                if 0 <= nr < len_r and 0 <= nc < len_c and matrix[r][c] > matrix[nr][nc]:
                    res = max(res, dp(nr, nc))
            return 1 + res

        ans = 0
        for r in range(len_r):
            for c in range(len_c):
                ans = max(ans, dp(r, c))
        return ans
# 0221 - Maximal Square
# Date: 2024-03-02
# Runtime: 528 ms, Memory: 19.3 MB
# Submission Id: 1191311642


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        len_r, len_c = len(matrix), len(matrix[0])
        max_len = 0

        dp = [0] * len_c
        for r in range(len_r):
            next_dp = [0] * len_c
            next_dp[0] = int(matrix[r][0] == '1')
            max_len = max(max_len, next_dp[0])
            for c in range(1, len_c):
                if matrix[r][c] == '0':
                    next_dp[c] = 0
                else:
                    next_dp[c] = 1 + min(next_dp[c-1], dp[c-1], dp[c])
                    max_len = max(max_len, next_dp[c])
            dp = next_dp

        return max_len * max_len
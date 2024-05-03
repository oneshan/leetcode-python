# 0967 - Minimum Falling Path Sum
# Date: 2024-05-02
# Runtime: 117 ms, Memory: 17.3 MB
# Submission Id: 1247246079


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        len_r, len_c = len(matrix), len(matrix[0])
        
        dp = matrix[0]
        for r in range(1, len_r):
            next_dp = [0] * len_c
            for c in range(len_c):
                min_prev = dp[c]
                if c > 0:
                    min_prev = min(min_prev, dp[c-1])
                if c < len_c-1:
                    min_prev = min(min_prev, dp[c+1])
                next_dp[c] = min_prev + matrix[r][c]
            dp = next_dp
                
        return min(dp)
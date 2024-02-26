# 0063 - Unique Paths II
# Date: 2024-02-23
# Runtime: 46 ms, Memory: 16.7 MB
# Submission Id: 1183600334


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
            
        len_r, len_c = len(obstacleGrid), len(obstacleGrid[0])

        dp = [0] * len_c
        dp[0] = 1
        for c in range(1, len_c):
            dp[c] = dp[c-1] & (obstacleGrid[0][c] == 0)

        for r in range(1, len_r):
            if obstacleGrid[r][0]:
                dp[0] = 0
            for c in range(1, len_c):
                dp[c] = 0 if obstacleGrid[r][c] else dp[c-1] + dp[c]
        return dp[-1]
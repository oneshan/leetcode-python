# 0063 - Unique Paths II
# Date: 2022-11-07
# Runtime: 95 ms, Memory: 14 MB
# Submission Id: 838688835


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        
        len_r, len_c = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * len_c for _ in range(len_r)]
        dp[0][0] = 1
        
        for i in range(1, len_r):
            dp[i][0] = 0 if obstacleGrid[i][0] == 1 else dp[i-1][0]
        for j in range(1, len_c):
            dp[0][j] = 0 if obstacleGrid[0][j] == 1 else dp[0][j-1]
            
        for r in range(1, len_r):
            for c in range(1, len_c):
                if obstacleGrid[r][c] == 0:
                    dp[r][c] = dp[r-1][c] + dp[r][c-1]
        return dp[-1][-1]
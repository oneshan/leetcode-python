# 0063 - Unique Paths II
# Date: 2024-05-02
# Runtime: 47 ms, Memory: 16.6 MB
# Submission Id: 1247233831


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        
        len_r, len_c = len(obstacleGrid), len(obstacleGrid[0])
        dp = [ [0] * len_c for _ in range(len_r)]
        dp[0][0] = 1
        
        for r in range(len_r):
            if obstacleGrid[r][0] == 1:
                break
            dp[r][0] = 1
            
        for c in range(len_c):
            if obstacleGrid[0][c] == 1:
                break
            dp[0][c] = 1
        
        for r in range(1, len_r):
            for c in range(1, len_c):
                if obstacleGrid[r][c] == 1:
                    dp[r][c] = 0
                else:
                    dp[r][c] = dp[r-1][c] + dp[r][c-1]
                    
        return dp[-1][-1]
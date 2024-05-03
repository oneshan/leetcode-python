# 0063 - Unique Paths II
# Date: 2024-05-02
# Runtime: 38 ms, Memory: 16.8 MB
# Submission Id: 1247236523


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        
        len_r, len_c = len(obstacleGrid), len(obstacleGrid[0])
        
        @cache
        def dp(r, c):
            if r == c == 0:
                return 1
            if r < 0 or c < 0:
                return 0
            if obstacleGrid[r][c] == 1:
                return 0
            return dp(r-1, c) + dp(r, c-1)
        
        return dp(len_r-1, len_c-1)
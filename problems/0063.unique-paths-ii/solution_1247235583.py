# 0063 - Unique Paths II
# Date: 2024-05-02
# Runtime: 38 ms, Memory: 16.7 MB
# Submission Id: 1247235583


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        
        len_r, len_c = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * len_c
        dp[0] = 1
        
        for r in range(len_r):
            for c in range(len_c):
                if obstacleGrid[r][c] == 1:
                    dp[c] = 0
                elif c:
                    dp[c] += dp[c-1]

        return dp[-1]
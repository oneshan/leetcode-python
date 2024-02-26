# 0688 - Knight Probability in Chessboard
# Date: 2022-10-16
# Runtime: 1261 ms, Memory: 14 MB
# Submission Id: 823586063


class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        if k == 0:
            return 1
        
        directions = [(-2,1), (-1,2), (1,2), (2,1),
                      (-2,-1), (-1,-2), (1,-2), (2,-1)]
        dp = [[0]*n for _ in range(n)]
        dp[row][column] = 1

        for _ in range(k):
            dp2 = [[0]*n for _ in range(n)]
            for r in range(n):
                for c in range(n):
                    for dx, dy in directions:
                        new_x, new_y = r+dx, c+dy
                        if 0 <= new_x < n and 0 <= new_y < n:
                            dp2[new_x][new_y] += dp[r][c] / 8.0
            dp = dp2

        return sum(map(sum, dp))
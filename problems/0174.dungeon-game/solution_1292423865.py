# 0174 - Dungeon Game
# Date: 2024-06-18
# Runtime: 87 ms, Memory: 17.5 MB
# Submission Id: 1292423865


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        len_r, len_c = len(dungeon), len(dungeon[0])

        dp = [[float('inf')] * (len_c+1) for _ in range(len_r+1)]
        dp[len_r][len_c-1] = dp[len_r-1][len_c] = 1

        for r in range(len_r-1, -1, -1):
            for c in range(len_c-1, -1, -1):
                dp[r][c] = max(1, min(dp[r][c+1], dp[r+1][c]) - dungeon[r][c])

        return dp[0][0]
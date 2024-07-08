# 0174 - Dungeon Game
# Date: 2024-06-18
# Runtime: 91 ms, Memory: 17.8 MB
# Submission Id: 1292426909


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        len_r, len_c = len(dungeon), len(dungeon[0])

        dp = [float('inf')] * (len_c+1)
        dp[len_c] = dp[len_c-1] = 1

        for r in range(len_r-1, -1, -1):
            next_dp = [float('inf')] * (len_c+1)
            for c in range(len_c-1, -1, -1):
                next_dp[c] = max(1, min(dp[c], next_dp[c+1]) - dungeon[r][c])
            dp = next_dp

        return dp[0]
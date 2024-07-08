# 0174 - Dungeon Game
# Date: 2024-06-18
# Runtime: 72 ms, Memory: 19.9 MB
# Submission Id: 1292429518


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        len_r, len_c = len(dungeon), len(dungeon[0])

        @cache
        def dp(r, c):
            if r == len_r-1 and c == len_c-1:
                return max(1, 1-dungeon[r][c])
            
            if r == len_r or c == len_c:
                return float('inf')

            return max(1, min(dp(r+1, c), dp(r, c+1)) - dungeon[r][c])

        return dp(0, 0)
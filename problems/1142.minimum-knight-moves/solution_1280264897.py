# 1142 - Minimum Knight Moves
# Date: 2024-06-07
# Runtime: 49 ms, Memory: 17.7 MB
# Submission Id: 1280264897


class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:

        @cache        
        def dfs(x, y):
            if x == y == 0:
                return 0
            
            # (1, 1), (0, 2), (2, 0)
            if x + y == 2:
                return 2

            return 1 + min(dfs(abs(x-1), abs(y-2)), dfs(abs(x-2), abs(y-1)))

        return dfs(abs(x), abs(y))
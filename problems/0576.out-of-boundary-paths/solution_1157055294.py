# 0576 - Out of Boundary Paths
# Date: 2024-01-26
# Runtime: 71 ms, Memory: 22.7 MB
# Submission Id: 1157055294


class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 1_000_000_007
        
        @cache
        def recur(row, col, move):
            if row < 0 or row == m or col < 0 or col == n:
                return 1
            if move == 0:
                return 0
            
            res = 0
            for dr, dc in (0, 1), (0, -1), (1, 0), (-1, 0):
                res += recur(row + dr, col + dc, move - 1) % MOD
            return res
        
        return recur(startRow, startColumn, maxMove) % MOD
# 1559 - Cherry Pickup II
# Date: 2024-02-11
# Runtime: 1094 ms, Memory: 37.8 MB
# Submission Id: 1172146047


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        len_r, len_c = len(grid), len(grid[0])

        @cache
        def recur(r, c1, c2):
            if r == len_r:
                return 0
            res = grid[r][c1]
            if c1 != c2:
                res += grid[r][c2]
            res += max(
                recur(r+1, min(n1, n2), max(n1, n2))
                for n1 in range(max(0, c1-1), min(len_c, c1+2))
                for n2 in range(max(0, c2-1), min(len_c, c2+2))
            )
            return res
        
        return recur(0, 0, len_c-1)
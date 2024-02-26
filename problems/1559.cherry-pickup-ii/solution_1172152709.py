# 1559 - Cherry Pickup II
# Date: 2024-02-11
# Runtime: 1264 ms, Memory: 17 MB
# Submission Id: 1172152709


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        len_r, len_c = len(grid), len(grid[0])

        dp = [[0] * len_c for _ in range(len_c)]
        for r in range(len_r-1, -1, -1):
            next_dp = [[0] * len_c for _ in range(len_c)]
            for c1 in range(len_c):
                for c2 in range(len_c):
                    res = grid[r][c1]
                    if c1 != c2:
                        res += grid[r][c2]
                    res += max(
                        dp[n1][n2]
                        for n1 in (c1-1, c1, c1+1)
                        for n2 in (c2-1, c2, c2+1)
                        if 0 <= n1 < len_c and 0 <= n2 < len_c
                    )
                    next_dp[c1][c2] = res
            dp = next_dp
        return dp[0][-1]
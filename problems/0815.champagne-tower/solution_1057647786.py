# 0815 - Champagne Tower
# Date: 2023-09-24
# Runtime: 74 ms, Memory: 16.4 MB
# Submission Id: 1057647786


class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0] * i for i in range(1, 102)]
        dp[0][0] = poured
        for r in range(query_row+1):
            for c in range(r+1):
                q = (dp[r][c] - 1) / 2
                if q > 0:
                    dp[r+1][c] += q
                    dp[r+1][c+1] += q
        return min(1, dp[query_row][query_glass])
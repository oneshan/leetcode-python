# 0576 - Out of Boundary Paths
# Date: 2024-01-26
# Runtime: 195 ms, Memory: 16.9 MB
# Submission Id: 1157062656


class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 1_000_000_007
        
        dp = [[0] * n for _ in range(m)]
        dp[startRow][startColumn] = 1

        count = 0
        for _ in range(maxMove):
            new_dp = [[0] * n for _ in range(m)]
            for row in range(m):
                for col in range(n):

                    for dr, dc in (0, 1), (0, -1), (1, 0), (-1, 0):
                        new_r, new_c = row + dr, col + dc
                        if 0 <= new_r < m and 0 <= new_c < n:
                            new_dp[row][col] += dp[new_r][new_c]
                        else:
                            count = (count + dp[row][col]) % MOD


                    new_dp[row][col] %= MOD
            dp = new_dp
        
        return count
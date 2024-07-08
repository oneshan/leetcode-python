# 0552 - Student Attendance Record II
# Date: 2024-05-26
# Runtime: 1821 ms, Memory: 16.4 MB
# Submission Id: 1268176794


class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 1_000_000_007

        dp = [[0] * 3 for i in range(2)]
        # dp[absent][late]

        dp[0][0] = 1
        for i in range(n):
            next_dp = [[0] * 3 for i in range(2)]
            # A
            next_dp[1][0] = (dp[0][0] + dp[0][1] + dp[0][2]) % MOD
            for j in range(2):
                # P
                next_dp[j][0] += (dp[j][0] + dp[j][1] + dp[j][2]) % MOD
                # L
                next_dp[j][1] = dp[j][0]
                next_dp[j][2] = dp[j][1]
            dp = next_dp

        return (sum(dp[0]) + sum(dp[1])) % MOD
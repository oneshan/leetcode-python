# 0972 - Knight Dialer
# Date: 2023-11-27
# Runtime: 642 ms, Memory: 16.3 MB
# Submission Id: 1107334624


class Solution:
    def knightDialer(self, n: int) -> int:
        next_d = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [3, 9, 0],
            5: [],
            6: [1, 7, 0],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4],
        }
        
        ans = 0
        MOD = 1_000_000_007
        
        prev_dp = [1] * 10
        for _ in range(n-1):
            dp = [0] * 10
            for i in range(10):
                for j in next_d[i]:
                    dp[j] = (dp[j] + prev_dp[i]) % MOD
            prev_dp = dp
            
        return sum(prev_dp) % MOD
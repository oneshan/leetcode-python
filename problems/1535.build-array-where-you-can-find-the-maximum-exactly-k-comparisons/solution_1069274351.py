# 1535 - Build Array Where You Can Find The Maximum Exactly K Comparisons
# Date: 2023-10-07
# Runtime: 739 ms, Memory: 43.4 MB
# Submission Id: 1069274351


class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:

        MOD = 10 ** 9 + 7

        @cache
        def dp(i, curr_max, remains):
            if i == n:
                return int(remains == 0)
            
            count = curr_max * dp(i+1, curr_max, remains) % MOD
            for next_max in range(curr_max+1, m+1):
                count += dp(i+1, next_max, remains-1)
            return count % MOD
        
        return dp(0, 0, k)
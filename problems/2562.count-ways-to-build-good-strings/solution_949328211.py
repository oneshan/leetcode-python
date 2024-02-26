# 2562 - Count Ways To Build Good Strings
# Date: 2023-05-13
# Runtime: 3522 ms, Memory: 678.1 MB
# Submission Id: 949328211


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [0] * (high+1)        
        dp[0] = 1

        mod = 10**9 + 7
        for i in range(1, high+1):
            if i >= zero:
                dp[i] += dp[i-zero]
            if i >= one:
                dp[i] += dp[i-one]

        curr_sum = 0
        for i in range(low, high+1):
            curr_sum += dp[i] % mod
        return curr_sum % mod
# 2562 - Count Ways To Build Good Strings
# Date: 2022-11-12
# Runtime: 933 ms, Memory: 17.8 MB
# Submission Id: 842028224


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [0] * (high+1)        
        dp[0] = 1

        mod = 10**9 + 7
        for i in range(high+1):
            if i + zero <= high:
                dp[i+zero] = (dp[i+zero] + dp[i]) % mod
            if i + one <= high:
                dp[i+one] = (dp[i+one] + dp[i]) % mod

        curr_sum = 0
        for i in range(low, high+1):
            curr_sum += dp[i] % mod
        return curr_sum % mod
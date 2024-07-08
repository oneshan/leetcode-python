# 0650 - 2 Keys Keyboard
# Date: 2024-06-11
# Runtime: 35 ms, Memory: 16.5 MB
# Submission Id: 1284682891


class Solution:
    def minSteps(self, n: int) -> int:

        @cache
        def dp(n):
            if n == 1:
                return 0
            i, ans = 2, n
            while i * i <= n:
                if n % i == 0:
                    ans = min(ans, dp(n // i) + i)
                i += 1
            return ans

        return dp(n)
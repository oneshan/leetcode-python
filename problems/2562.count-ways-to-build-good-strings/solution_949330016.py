# 2562 - Count Ways To Build Good Strings
# Date: 2023-05-13
# Runtime: 325 ms, Memory: 134 MB
# Submission Id: 949330016


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = 10**9 + 7
        
        @cache
        def dfs(i):
            if i == 0:
                return 1
            if i < 0:
                return 0
            return (dfs(i-zero) + dfs(i-one)) % mod

        ans = 0
        for i in range(low, high+1):
            ans += dfs(i)
        return ans % mod
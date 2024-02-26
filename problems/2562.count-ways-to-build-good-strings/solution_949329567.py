# 2562 - Count Ways To Build Good Strings
# Date: 2023-05-13
# Runtime: 329 ms, Memory: 129 MB
# Submission Id: 949329567


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = 10**9 + 7
        
        @cache
        def dfs(i):
            if i == 0:
                return 1
            count = 0
            if i >= zero:
                count += dfs(i-zero)
            if i >= one:
                count += dfs(i-one)
            return count % mod

        ans = 0
        for i in range(low, high+1):
            ans += dfs(i)
        return ans % mod
# 2325 - Number of Ways to Select Buildings
# Date: 2024-07-17
# Runtime: 365 ms, Memory: 17.6 MB
# Submission Id: 1323559943


class Solution:
    def numberOfWays(self, s: str) -> int:
        n = len(s)
        ones = sum(ch == '1' for ch in s)
        zeros = n - ones

        ans = c0 = c1 = 0
        for ch in s:
            if ch == '1':
                ans += c0 * (zeros - c0)
                c1 += 1
            else:
                ans += c1 * (ones - c1)
                c0 += 1
        return ans
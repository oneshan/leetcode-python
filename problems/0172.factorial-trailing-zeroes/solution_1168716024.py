# 0172 - Factorial Trailing Zeroes
# Date: 2024-02-07
# Runtime: 34 ms, Memory: 16.5 MB
# Submission Id: 1168716024


class Solution:
    def trailingZeroes(self, n: int) -> int:
        five, ans = 5, 0
        while five <= n:
            ans += n // five
            five *= 5
        return ans
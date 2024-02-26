# 0371 - Sum of Two Integers
# Date: 2024-02-07
# Runtime: 40 ms, Memory: 16.5 MB
# Submission Id: 1168566597


class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = (1 << 32) - 1
        max_int = (1 << 31) - 1
        while b:
            a, b = (a^b) & mask, ((a&b)<<1) & mask
        return a if a < max_int else ~(a ^ mask)
# 0371 - Sum of Two Integers
# Date: 2024-05-11
# Runtime: 36 ms, Memory: 16.5 MB
# Submission Id: 1255337154


class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF

        while b != 0:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask

        max_int = 0x7FFFFFFF
        return a if a < max_int else ~(a ^ mask)
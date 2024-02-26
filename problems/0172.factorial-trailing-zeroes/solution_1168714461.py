# 0172 - Factorial Trailing Zeroes
# Date: 2024-02-07
# Runtime: 44 ms, Memory: 16.5 MB
# Submission Id: 1168714461


class Solution:
    def trailingZeroes(self, n: int) -> int:
        mult5 = [5 ** i for i in range(1, 6)]
        return sum(n // x for x in mult5)
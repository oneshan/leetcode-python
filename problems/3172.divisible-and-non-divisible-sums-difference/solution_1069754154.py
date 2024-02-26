# 3172 - Divisible and Non-divisible Sums Difference
# Date: 2023-10-08
# Runtime: 38 ms, Memory: 16.3 MB
# Submission Id: 1069754154


class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:

        divisible = 0
        for i in range(m, n+1, m):
            divisible += i
        
        not_divisible = (1 + n) * n // 2 - divisible
        return not_divisible - divisible
        
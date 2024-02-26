# 0263 - Ugly Number
# Date: 2022-11-18
# Runtime: 58 ms, Memory: 13.9 MB
# Submission Id: 845718085


class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 2 == 0:
            n //= 2
        while n % 3 == 0:
            n //= 3
        while n % 5 == 0:
            n //= 5
        return n == 1
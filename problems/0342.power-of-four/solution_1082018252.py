# 0342 - Power of Four
# Date: 2023-10-23
# Runtime: 38 ms, Memory: 16.2 MB
# Submission Id: 1082018252


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        while n > 1:
            if n & 1 or n & 2:
                return False
            n >>= 2
        return n == 1
# 0342 - Power of Four
# Date: 2023-10-23
# Runtime: 39 ms, Memory: 16.3 MB
# Submission Id: 1082020481


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and n & (n-1) == 0 and n % 3 == 1
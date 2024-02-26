# 0069 - Sqrt(x)
# Date: 2024-02-07
# Runtime: 26 ms, Memory: 16.5 MB
# Submission Id: 1168722014


class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        left = self.mySqrt(x >> 2) << 1
        right = left + 1
        return left if right * right > x else right
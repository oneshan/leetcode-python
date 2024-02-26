# 0050 - Pow(x, n)
# Date: 2024-02-07
# Runtime: 37 ms, Memory: 16.7 MB
# Submission Id: 1168723966


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n == 0:
            return 1
        if n == 1:
            return x
        half = self.myPow(x, n >> 1)
        return (x if n & 1 else 1) * half * half
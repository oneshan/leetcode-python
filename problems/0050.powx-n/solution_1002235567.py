# 0050 - Pow(x, n)
# Date: 2023-07-24
# Runtime: 35 ms, Memory: 16.2 MB
# Submission Id: 1002235567


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1.0 / self.myPow(x, -n)
        if n == 0:
            return 1
        half = self.myPow(x, n//2)
        if n & 1:
            return x * half * half
        return half * half
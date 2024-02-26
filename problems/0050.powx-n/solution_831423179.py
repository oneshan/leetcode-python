# 0050 - Pow(x, n)
# Date: 2022-10-27
# Runtime: 60 ms, Memory: 13.9 MB
# Submission Id: 831423179


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n == 0:
            return 1
        if n & 1:
            return x * self.myPow(x, n-1)
            
        val = self.myPow(x, n >> 1)
        return val * val
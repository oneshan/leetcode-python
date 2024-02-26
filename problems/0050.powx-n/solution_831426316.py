# 0050 - Pow(x, n)
# Date: 2022-10-27
# Runtime: 74 ms, Memory: 13.8 MB
# Submission Id: 831426316


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        if n < 0:
            x, n = 1/x, -n
            
        ans, curr = 1, x
        while n:
            if n & 1:
                ans *= curr
            curr *= curr
            n >>= 1
        return ans
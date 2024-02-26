# 0371 - Sum of Two Integers
# Date: 2024-02-07
# Runtime: 38 ms, Memory: 16.5 MB
# Submission Id: 1168746641


class Solution:
    def getSum(self, a: int, b: int) -> int:
        x, y = abs(a), abs(b)
        if x < y:
            return self.getSum(b, a)

        sign = 1 if a > 0 else -1
        if a * b >= 0:
            # x + y
            while y:
                x, y = (x^y), (x&y)<<1
        else:
            # x - y
            while y:
                x, y = (x^y), ((~x)&y)<<1

        return x * sign
# 0633 - Sum of Square Numbers
# Date: 2022-11-29
# Runtime: 162 ms, Memory: 13.8 MB
# Submission Id: 851272030


from math import isqrt
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for a in range(c+1):
            square_b = c - a*a
            if square_b < 0:
                return False
            b = isqrt(square_b)
            if b * b == square_b:
                return True
        return False
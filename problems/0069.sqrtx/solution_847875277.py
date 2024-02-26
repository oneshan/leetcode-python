# 0069 - Sqrt(x)
# Date: 2022-11-22
# Runtime: 83 ms, Memory: 13.8 MB
# Submission Id: 847875277


from math import e, log

class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        left = int(e**(0.5 * log(x)))
        right = left + 1
        return left if right * right > x else right
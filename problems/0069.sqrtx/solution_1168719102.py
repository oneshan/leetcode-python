# 0069 - Sqrt(x)
# Date: 2024-02-07
# Runtime: 41 ms, Memory: 16.5 MB
# Submission Id: 1168719102


class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 1, x+1
        while left < right:
            mid = (left + right) // 2
            square = mid * mid
            if square == x:
                return mid
            if square > x:
                right = mid
            else:
                left = mid + 1
        return left - 1
# 0069 - Sqrt(x)
# Date: 2022-11-22
# Runtime: 42 ms, Memory: 13.8 MB
# Submission Id: 847873207


class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 1, x
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            if square == x:
                return mid
            if square < x:
                left = mid + 1
            else:
                right = mid - 1
        return right
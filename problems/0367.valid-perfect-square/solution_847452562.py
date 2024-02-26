# 0367 - Valid Perfect Square
# Date: 2022-11-21
# Runtime: 21 ms, Memory: 13.8 MB
# Submission Id: 847452562


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 1, num
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            if square == num:
                return True
            if square < num:
                left = mid + 1
            else:
                right = mid - 1
        return False
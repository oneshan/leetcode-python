# 0633 - Sum of Square Numbers
# Date: 2022-11-29
# Runtime: 8127 ms, Memory: 13.9 MB
# Submission Id: 851274407


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        def binary_search(left, right, target):
            while left <= right:
                mid = (left + right) // 2
                square =  mid * mid
                if square == target:
                    return True
                if square > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return False
        
        for a in range(c+1):
            square_b = c - a*a
            if square_b < 0:
                break
            if binary_search(a, c, square_b):
                return True
        return False
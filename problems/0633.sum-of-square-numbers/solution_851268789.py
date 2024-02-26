# 0633 - Sum of Square Numbers
# Date: 2022-11-29
# Runtime: 7233 ms, Memory: 13.9 MB
# Submission Id: 851268789


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c < 3:
            return True
        
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
        
        for i in range(c):
            target = c - i*i
            if target < 0:
                break
            if binary_search(i, c, target):
                return True
        return False
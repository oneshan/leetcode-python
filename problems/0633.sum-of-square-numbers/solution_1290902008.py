# 0633 - Sum of Square Numbers
# Date: 2024-06-17
# Runtime: 1717 ms, Memory: 16.5 MB
# Submission Id: 1290902008


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        for i in range(int(sqrt(c))+1):
            target = c - i * i
            left, right = i, c
            while left <= right:
                mid = (left + right) // 2        
                square = mid * mid
                if square == target:
                    return True
                if square < target:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return False
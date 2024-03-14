# 2571 - Find the Pivot Integer
# Date: 2024-03-13
# Runtime: 43 ms, Memory: 16.5 MB
# Submission Id: 1202093471


class Solution:
    def pivotInteger(self, n: int) -> int:
        if n == 1:
            return 1

        left, right = 1, n
        sum_left = sum_right = 0
        while left < right:
            if sum_left < sum_right:
                sum_left += left
                left += 1
            else:
                sum_right += right
                right -= 1
            if sum_left == sum_right and left == right:
                return left
        
        return -1
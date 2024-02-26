# 1929 - Maximum Value at a Given Index in a Bounded Array
# Date: 2023-06-10
# Runtime: 62 ms, Memory: 16.2 MB
# Submission Id: 968014437


class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        
        def check(val):
            left = max(0, val - index - 1)
            right = max(0, val - n + index)
            return val ** 2 <= maxSum + (left * (left+1)) // 2 + right * (right+1) // 2
        
        maxSum -= n
        left, right = 0, maxSum
        while left < right:
            mid = (left + right + 1) // 2
            if check(mid):
                left = mid
            else:
                right = mid - 1
        return left + 1
# 0279 - Perfect Squares
# Date: 2024-02-08
# Runtime: 117 ms, Memory: 27.2 MB
# Submission Id: 1169368351


class Solution:
    def numSquares(self, n: int) -> int:
        square = {i * i for i in range(0, 101)}
        
        @cache
        def is_perfect(num, step):
            if step == 1:
                return num in square
            for s in square:
                if num > s and is_perfect(num-s, step-1):
                    return True
            return False


        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if is_perfect(n, mid):
                right = mid
            else:
                left = mid + 1
        return left
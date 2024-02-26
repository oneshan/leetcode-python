# 0279 - Perfect Squares
# Date: 2022-11-10
# Runtime: 356 ms, Memory: 14.2 MB
# Submission Id: 840610784


class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i * i for i in range(1, int(sqrt(n)+1))]
        
        def is_divided_by(n, step):
            if step == 1:
                return n in squares
            for k in squares:
                if n < k:
                    break
                if is_divided_by(n-k, step-1):
                    return True
            return False
        
        for i in range(1, n+1):
            if is_divided_by(n, i):
                return i
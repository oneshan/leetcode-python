# 0279 - Perfect Squares
# Date: 2022-10-28
# Runtime: 356 ms, Memory: 14 MB
# Submission Id: 832118081


class Solution:
    def numSquares(self, n: int) -> int:
        perfect = [i*i for i in range(1, int(n**0.5)+1)]
        
        def is_divided_by(n, step):
            if step == 1:
                return n in perfect
            for k in perfect:
                if n < k:
                    break
                if is_divided_by(n-k, step-1):
                    return True
            return False
        
        for i in range(1, n+1):
            if is_divided_by(n, i):
                return i
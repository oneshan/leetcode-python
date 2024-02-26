# 0279 - Perfect Squares
# Date: 2022-10-28
# Runtime: 115 ms, Memory: 14.3 MB
# Submission Id: 832108934


class Solution:
    def numSquares(self, n: int) -> int:
        perfect = set([i*i for i in range(1, int(n**0.5)+1)])
        
        def is_divided_by(n, step):
            if step == 1:
                return n in perfect
            for k in perfect:
                if n > k and is_divided_by(n-k, step-1):
                    return True
            return False
        
        for step in range(1, n+1):
            if is_divided_by(n, step):
                return step
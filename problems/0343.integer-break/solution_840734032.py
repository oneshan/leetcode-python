# 0343 - Integer Break
# Date: 2022-11-10
# Runtime: 56 ms, Memory: 13.8 MB
# Submission Id: 840734032


class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n-1
        
        p, q = divmod(n, 3)
        if q == 0:
            return 3 ** p
        if q == 1:
            return 3 ** (p-1) * 4
        if q == 2:
            return 3 ** p * 2
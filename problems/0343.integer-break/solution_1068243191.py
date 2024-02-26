# 0343 - Integer Break
# Date: 2023-10-06
# Runtime: 33 ms, Memory: 16.1 MB
# Submission Id: 1068243191


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
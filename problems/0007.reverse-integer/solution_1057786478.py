# 0007 - Reverse Integer
# Date: 2023-09-24
# Runtime: 44 ms, Memory: 16.2 MB
# Submission Id: 1057786478


class Solution:
    def reverse(self, x: int) -> int:
        is_neg = x < 0
        x = abs(x)
        
        num = 0
        while x:
            x, r = divmod(x, 10)
            num = (num * 10) + r
        
        if is_neg:
            num = -num
            
            
        return num if -(1<<31) <= num < (1<<31)-1 else 0
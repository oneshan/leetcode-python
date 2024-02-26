# 0202 - Happy Number
# Date: 2022-07-16
# Runtime: 45 ms, Memory: 13.8 MB
# Submission Id: 748363433


class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n > 1:
            if n in seen:
                return False
            seen.add(n)
            n = self.happy(n)
        return n == 1
    
    def happy(self, n):
        next_n = 0
        while n:
            n, b = divmod(n, 10)
            next_n += b * b
        return next_n
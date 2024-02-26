# 0202 - Happy Number
# Date: 2022-07-16
# Runtime: 48 ms, Memory: 13.9 MB
# Submission Id: 748365330


class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n > 1 and n not in seen:
            seen.add(n)
            n = self.happy(n)
        return n == 1
    
    def happy(self, n):
        next_n = 0
        while n:
            n, digit = divmod(n, 10)
            next_n += digit ** 2
        return next_n
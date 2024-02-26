# 0202 - Happy Number
# Date: 2022-07-16
# Runtime: 66 ms, Memory: 13.9 MB
# Submission Id: 748367615


class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.happy(n)
        while fast > 1:
            if fast == slow:
                break
            fast = self.happy(self.happy(fast))
            slow = self.happy(slow)
        return fast == 1
    
    def happy(self, n):
        next_n = 0
        while n:
            n, digit = divmod(n, 10)
            next_n += digit ** 2
        return next_n
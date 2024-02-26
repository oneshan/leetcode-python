# 0202 - Happy Number
# Date: 2022-09-14
# Runtime: 58 ms, Memory: 13.9 MB
# Submission Id: 799518041


class Solution:
    def isHappy(self, n: int) -> bool:
        def next_num(num):
            _next = 0
            while num:
                num, d = divmod(num, 10)
                _next += d * d
            return _next
        
        seen = set()
        while n > 1:
            if n in seen:
                return False
            seen.add(n)
            n = next_num(n)
        return True
    
    
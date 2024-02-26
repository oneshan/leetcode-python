# 0202 - Happy Number
# Date: 2022-11-12
# Runtime: 68 ms, Memory: 13.8 MB
# Submission Id: 841738673


class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while True:
            if n in seen:
                return False
            seen.add(n)
            next_n = 0
            while n:
                n, r = divmod(n, 10)
                next_n += r ** 2
            if next_n == 1:
                return True
            n = next_n
        return True
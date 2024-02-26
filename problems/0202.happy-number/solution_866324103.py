# 0202 - Happy Number
# Date: 2022-12-27
# Runtime: 36 ms, Memory: 13.8 MB
# Submission Id: 866324103


class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            seen.add(n)
            next_n = 0
            while n:
                n, digit = divmod(n, 10)
                next_n += digit * digit
            if next_n == 1:
                return True
            n = next_n
        return False
# 0202 - Happy Number
# Date: 2024-02-10
# Runtime: 39 ms, Memory: 16.5 MB
# Submission Id: 1171066481


class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            if n == 1:
                return True
            seen.add(n)
            next_n = 0
            while n:
                n, digit = divmod(n, 10)
                next_n += digit * digit
            n = next_n

        return False
# 0804 - Rotated Digits
# Date: 2024-06-02
# Runtime: 59 ms, Memory: 16.4 MB
# Submission Id: 1274953529


class Solution:
    def rotatedDigits(self, n: int) -> int:
        s1 = {1, 8, 0, 2, 5, 6, 9}
        s2 = {2, 5, 6, 9}

        def is_good(num):
            is_diff = False
            while num:
                num, digit = divmod(num, 10)
                if digit not in s1:
                    return False
                if digit in s2:
                    is_diff = True
            return is_diff

        return sum(is_good(num) for num in range(1, n+1))
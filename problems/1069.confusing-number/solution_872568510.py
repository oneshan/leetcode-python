# 1069 - Confusing Number
# Date: 2023-01-06
# Runtime: 73 ms, Memory: 14 MB
# Submission Id: 872568510


class Solution:
    def confusingNumber(self, n: int) -> bool:
        mapping = {
            0: 0,
            1: 1,
            6: 9,
            9: 6,
            8: 8,
        }
        next_n = 0
        temp = n
        while temp:
            temp, r = divmod(temp, 10)
            if r not in mapping:
                return False
            next_n = next_n * 10 + mapping[r]
        return next_n != n
# 0258 - Add Digits
# Date: 2023-04-26
# Runtime: 30 ms, Memory: 13.8 MB
# Submission Id: 939871697


class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            total = 0
            while num:
                num, d = divmod(num, 10)
                total += d
            num = total
        return num
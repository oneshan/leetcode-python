# 0258 - Add Digits
# Date: 2023-04-26
# Runtime: 37 ms, Memory: 13.8 MB
# Submission Id: 939874021


class Solution:
    def addDigits(self, num: int) -> int:
        return 1 + (num-1) % 9 if num else 0
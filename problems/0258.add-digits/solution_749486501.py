# 0258 - Add Digits
# Date: 2022-07-17
# Runtime: 58 ms, Memory: 13.8 MB
# Submission Id: 749486501


class Solution:
    def addDigits(self, num: int) -> int:
        return 1 + (num-1) % 9 if num else 0
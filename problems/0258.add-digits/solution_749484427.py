# 0258 - Add Digits
# Date: 2022-07-17
# Runtime: 54 ms, Memory: 13.9 MB
# Submission Id: 749484427


class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            next_num = 0
            while num > 0:
                num, r = divmod(num, 10)
                next_num += r
            num = next_num
        return num
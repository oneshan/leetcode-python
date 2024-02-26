# 0507 - Perfect Number
# Date: 2022-11-22
# Runtime: 64 ms, Memory: 13.9 MB
# Submission Id: 847980375


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num < 2:
            return False

        i, total = 2, 1
        while i * i < num:
            if num % i == 0:
                total += i + num // i
            i += 1
        return total == num
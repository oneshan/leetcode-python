# 0202 - Happy Number
# Date: 2022-07-24
# Runtime: 60 ms, Memory: 13.8 MB
# Submission Id: 755481413


class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            total_sum = 0
            while n:
                total_sum += (n % 10) ** 2
                n //= 10
            n = total_sum
        return n == 1
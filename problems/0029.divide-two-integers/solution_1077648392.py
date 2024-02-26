# 0029 - Divide Two Integers
# Date: 2023-10-18
# Runtime: 40 ms, Memory: 16.4 MB
# Submission Id: 1077648392


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == -1 and dividend == -2147483648:
            return 2147483647

        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        dividend, divisor = abs(dividend), abs(divisor)        
        
        ans = 0
        while dividend >= divisor:
            k, curr = 1, divisor
            while dividend >= curr:
                dividend -= curr
                ans += k
                k <<= 1
                curr <<= 1

        return ans * sign